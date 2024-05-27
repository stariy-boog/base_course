import matplotlib.pyplot as plt
from scipy import interpolate
import shapely.geometry as geom
import numpy as np

image = plt.imread('crab.png')
fig, ax = plt.subplots()
ax.imshow(image, extent=[-650, 650, 650, -650])

def x_cloud_coords():
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
    return x
def y_cloud_coords():
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
    return y

def x_void_coords_1():
    t = np.linspace(-np.pi/4, np.pi/6, 100)
    x1 = -80 + 50 * np.cos(t)
    y1 = 340 - 70 * np.sin(t)

    t = np.linspace(np.pi/2, -np.pi, 100)
    x2 = 100 * np.cos(t)
    y2 = 200 + 100 * np.sin(t)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    t = np.linspace(0 , np.pi/2, 100)
    x1 = -251 + 150 * np.cos(t)
    y1 = 200 + 50 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi/2.5, -np.pi*3/4, 100)
    x1 = -330 + 250 * np.cos(t)
    y1 = 485 + 250 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -505
    y1 = 445

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi*4/3, -np.pi*5/3, 100)
    x1 = -450 + 100 * np.cos(t)
    y1 = 350 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -385
    y1 = 450

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -380
    y1 = 500

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi*11/18, -np.pi/6, 100)
    x1 = -210 + 500 * np.cos(t)
    y1 = 220 - 300 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -40
    y1 = 390

    x = np.append(x, x1)
    y = np.append(y, y1)

    return x
def y_void_coords_1():
    t = np.linspace(-np.pi/4, np.pi/6, 100)
    x1 = -80 + 50 * np.cos(t)
    y1 = 340 - 70 * np.sin(t)

    t = np.linspace(np.pi/2, -np.pi, 100)
    x2 = 100 * np.cos(t)
    y2 = 200 + 100 * np.sin(t)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    t = np.linspace(0 , np.pi/2, 100)
    x1 = -251 + 150 * np.cos(t)
    y1 = 200 + 50 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi/2.5, -np.pi*3/4, 100)
    x1 = -330 + 250 * np.cos(t)
    y1 = 485 + 250 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -505
    y1 = 445

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi*4/3, -np.pi*5/3, 100)
    x1 = -450 + 100 * np.cos(t)
    y1 = 350 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -385
    y1 = 450

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -380
    y1 = 500

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi*11/18, -np.pi/6, 100)
    x1 = -210 + 500 * np.cos(t)
    y1 = 220 - 300 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    x1 = -40
    y1 = 390

    x = np.append(x, x1)
    y = np.append(y, y1)

    return y

def x_void_coords_2():
    t = np.linspace(np.pi/20, -np.pi/6, 100)
    x1 = 380 + 180 * np.cos(t)
    y1 = -250 - 230 * np.sin(t)

    t = np.linspace(np.pi/30, -np.pi/4, 100)
    x2 = 330 + 200 * np.cos(t)
    y2 = 85 - 310 * np.sin(t)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    t = np.linspace(np.pi/2, np.pi, 100)
    x1 = 475 + 80 * np.cos(t)
    y1 = 220 + 80 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(np.pi/2, -np.pi/3, 100)
    x1 = 400 + 60 * np.cos(t)
    y1 = 120 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi/2, np.pi/16, 100)
    x1 = 470 + 60 * np.cos(t)
    y1 = 100 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    return x

def y_void_coords_2():
    t = np.linspace(np.pi/20, -np.pi/6, 100)
    x1 = 380 + 180 * np.cos(t)
    y1 = -250 - 230 * np.sin(t)

    t = np.linspace(np.pi/30, -np.pi/4, 100)
    x2 = 330 + 200 * np.cos(t)
    y2 = 85 - 310 * np.sin(t)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    t = np.linspace(np.pi/2, np.pi, 100)
    x1 = 475 + 80 * np.cos(t)
    y1 = 220 + 80 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(np.pi/2, -np.pi/3, 100)
    x1 = 400 + 60 * np.cos(t)
    y1 = 120 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    t = np.linspace(-np.pi/2, np.pi/16, 100)
    x1 = 470 + 60 * np.cos(t)
    y1 = 100 + 100 * np.sin(t)

    x = np.append(x, x1)
    y = np.append(y, y1)

    return y

def make_curve(x, y):
    spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
    spline_curve = interpolate.splev(figure_spline_part, spline_coords)

    plt.plot(spline_curve[0], spline_curve[1], 'w')
    curve = []
    points = []
    for i in range(len(spline_curve[0])):
        curve.append([spline_curve[0][i], spline_curve[1][i]])

    return curve, points

curve_coords, points_coords = make_curve(x_cloud_coords(), y_cloud_coords())
first_void_curve, first_void_points = make_curve(x_void_coords_1(), y_void_coords_1())
second_void_curve, second_void_point = make_curve(x_void_coords_2(), y_void_coords_2())

second_void_polygon = geom.Polygon(second_void_curve)
first_void_polygon = geom.Polygon(first_void_curve)
cloud_polygon = geom.Polygon(curve_coords)

points_number_per_side = 50
x_pictures_limits = [-650, 650]
y_pictures_limits = [650, -650]
void_points = 0

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(first_void_polygon):
            continue
        elif p.within(second_void_polygon):
            continue
        elif p.within(cloud_polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)
        
#SCALAR FIELDS
x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_field = intensity*np.exp(-dec_rate[0] * x**2 - dec_rate[1] * y**2)
    return scalar_field

intensity_centrums_x = [-350, -150, 420, 490, -500, -10, 200, 300, 450, -400, -50, -500, 200, 0, 200]            

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

#VECTORS
x, y = np.meshgrid(np.linspace(-650, -500, 4), np.linspace(200, 400, 4))
u = -3
v = 8
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(-600, -450, 5), np.linspace(-200, 150, 5))
u = -4
v = 5
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(-400, -300, 3), np.linspace(-400, 0, 4))
u = 2
v = 10
plt.quiver(x, y, u, v, width=0.005)
x, y = np.meshgrid(np.linspace(-250, -150, 3), np.linspace(-400, 0, 4))
u = -5
v = 10
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(-350, -200, 3), np.linspace(50, 200, 3))
u = -10
v = 4
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(-100, -100, 1), np.linspace(-600, 100, 10))
u = -2
v = 5
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(-50, -50, 1), np.linspace(-600, 100, 10))
u = 2
v = 3
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(0, 0, 1), np.linspace(-600, 100, 10))
u = 2
v = 2
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(100, 100, 1), np.linspace(-200, 100, 4))
u = 0
v = 3
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(100, 100, 1), np.linspace(-450, -300, 3))
u = -5
v = 5
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(150, 225, 2), np.linspace(250, -300, 6))
u = 4
v = 3
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(175, 500, 6), np.linspace(-600, -400, 3))
u = -10
v = 8
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(350, 525, 3), np.linspace(-350, 400, 9))
u = -10
v = 12
plt.quiver(x, y, u, v, width=0.005)

x, y = np.meshgrid(np.linspace(0, 200, 3), np.linspace(340, 380, 2))
u = 10
v = 14
plt.quiver(x, y, u, v, width=0.005)

cbar = fig.colorbar(sc_plot)
cbar.set_label('Излучение радиоволн (Интенсивность)')
plt.savefig("homework_crab_nebula_scalar_fields.png")