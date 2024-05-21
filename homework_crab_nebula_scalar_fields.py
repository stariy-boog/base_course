import matplotlib.pyplot as plt
from scipy import interpolate
import shapely.geometry as geom
import numpy as np

image = plt.imread('crab.png')
fig, ax = plt.subplots()
ax.imshow(image, extent=[-650, 650, 650, -650])


t = np.linspace(np.pi, np.pi/2.5, 100)
x1 = -250 + 180 * np.cos(t)
y1 = -150 - 220 * np.sin(t)
x2 = -230
y2 = -410

x = np.append(x1, x2)
y = np.append(y1, y2)

x1 = -190
y1 = -420

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi, np.pi/8, 100)
x1 = -50 + 150 * np.cos(t)
y1 = -450 - 180 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi*2/3, np.pi/20, 100)
x1 =  350 + 180 * np.cos(t)
y1 = -350 - 230 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi/6, -np.pi/6, 100)
x1 = 380 + 180 * np.cos(t)
y1 = -250 - 230 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi/30, -np.pi*2/3, 100)
x1 = 330 + 200 * np.cos(t)
y1 = 85 - 310 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi/6, -np.pi*11/18, 100)
x1 = -210 + 500 * np.cos(t)
y1 = 220 - 300 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

x1 = -385
y1 = 450

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi/3, -np.pi*5/4, 100)
x1 = -465 + 160 * np.cos(t)
y1 = 300 - 150 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi*7/9, -np.pi*277/180, 100)
x1 = -450 + 160 * np.cos(t)
y1 = 50 - 163 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

x1 = -430
y1 = -150

x = np.append(x, x1)
y = np.append(y, y1)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.axis('equal')
plt.plot(spline_curve[0], spline_curve[1], 'w')

curve_coords = []
points_coords = []

for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 50
x_pictures_limits = [-650, 650]
y_pictures_limits = [650, -650]

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

intensity_centrums_x = [-350, -150, 480, 520, -500, -10, 200, 300, 450, -400, -50, -500, 200, 0, 200]            

intensity_centrums_y = [0, 125, 300, 0, 450, 500, -400, -250, -50, -200, -600, -150, 200, -200, 400]

intensity_values = [90, 90, 100, 100, 70, 70, 70, -10, 10, -10, -10, -10, 50, 10, -50]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x - int_cen_x[i], y - int_cen_y[i], 0.009, [0.00002, 0.00002])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centrums_x, intensity_centrums_y, intensity_values)
    scalar_fields.append(calculate)

sc_plot = ax.scatter(x_p, y_p, c=scalar_fields) 

ax.set_xlabel('Координата x, 43.7*10^9 световых лет')
ax.set_ylabel('Координата y, 43.7*10^9 световых лет')

cbar = fig.colorbar(sc_plot)
cbar.set_label('Излучение радиоволн (Интенсивность)')
plt.savefig("homework_crab_nebula_scalar_fields.png")