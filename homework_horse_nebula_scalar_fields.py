import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

image = plt.imread('horsead.jpg')
fig, ax = plt.subplots()

ax.imshow(image)

t = np.linspace(np.pi, 0, 100)
a = 50 + 47 * np.cos(t)
b = 290 - 10 * np.sin(t)

t = np.linspace(np.pi*7/6, np.pi/2, 100)
a1 = 138 + 47 * np.cos(t)
b1 = 275 - 30 * np.sin(t)

x = np.append(a, a1)
y = np.append(b, b1)

a = [140, 164]
b = [246, 115]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(-np.pi/14, -(np.pi*5/6), 100)
a = 110 + 55 * np.cos(t)
b = 105 - 45 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [64, 90]
b = [126, 108]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(-(np.pi*2/3), np.pi/6, 100)
a = 103 + 25 * np.cos(t)
b = 84 - 28 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [126, 151]
b = [69, 43]

x = np.append(x, a)
y = np.append(y, b)

a = [150, 210]
b = [43, 72]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(np.pi*4/7, np.pi/8, 100)
a = 228 + 70 * np.cos(t)
b = 220 - 150 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [293, 270]
b = [160, 285]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(np.pi/2, np.pi, 100)
a = 270 + 30 * np.cos(t)
b = 350 - 64 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [0, 245]
b = [350, 350]

x = np.append(x, a)
y = np.append(y, b)

a = [0, 245]
b = [350, 350]

x = np.append(x, a)
y = np.append(y, b)

a = [0, 0]
b = [350, 320]

x = np.append(x, a)
y = np.append(y, b)

a = 0
b = 350

x = np.append(x, a)
y = np.append(y, b)

a = 4
b = 290

x = np.append(x, a)
y = np.append(y, b)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.axis('equal')
plt.xlim(0, 350)
#plt.plot(spline_curve[0], spline_curve[1], color='w')

curve_coords = []
points_coords = []

for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 55
x_pictures_limits = [0, 350]
y_pictures_limits = [350, 0]

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_field = intensity*np.exp(-dec_rate[0] * x**2 - dec_rate[1] * y**2)
    return scalar_field

intensity_centrums_x = [160, 170, 180, 190, 200, 215, 230, 250,                       #upper part
                        190, 190, 200, 195, 205, 195,                                 #middle part 
                        155,                                                          #lower part
                        100, 130, 125, 150, 180, 190, 200, 152, 255, 80]              #weak connections

intensity_centrums_y = [72, 75, 78, 81, 84, 85, 87, 95,                               #upper part
                        130, 130, 200, 180, 210, 225,                                 #middle part 
                        260,                                                          #lower part
                        300, 280, 300, 280, 245, 160, 110, 95, 110, 325]              #weak connections

intensity_values = [60, 90, 80, 70, 70, 60, 130, 60,                                  #upper part
                    70, 30, 120, 60, 60, 50,                                          #middle part 
                    125,                                                              #lower part
                    60, 60, 60, 60, 60, 60, 60, 60, 60, 60]                           #weak connections

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x - int_cen_x[i], y - int_cen_y[i], 0.0372, [0.0035, 0.0035])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centrums_x, intensity_centrums_y, intensity_values)
    scalar_fields.append(calculate)

sc_plot = ax.scatter(x_p, y_p, c=scalar_fields) 

ax.set_xlabel('Координата x, м')
ax.set_ylabel('Координата y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label('Скорость C^18 O      [КМ/С]')
plt.savefig("homework_horse_nebula_scalar_fields.png")