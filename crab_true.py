import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import shapely.geometry as geom 
import h5py
import random

left, right, down, up = 0, 1, 0, 1


class ParticlesGenerator:

    def __init__(self, N, x0=0, y0=0, intensity=[5, 5]):
        self.N = N
        self.x0 = x0
        self.y0 = y0
        self.intensity = intensity

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

        x = np.append(x, x1)/1200 + 650/1200
        y = np.append(y, y1)/1200 + 650/1200

        spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
        spline_curve = interpolate.splev(figure_spline_part, spline_coords)

        curve_coords = []
        for i in range(len(spline_curve[0])):
            curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
        
        plt.plot(x, y, 'bo')
        plt.savefig('crab_true.png')

        self.polygon = geom.Polygon(curve_coords)

    def density(self, x, y):  
        return np.exp(- self.intensity[0] * (x - self.x0)**2 - self.intensity[1] * (y - self.y0)**2)

    def points_generator(self):

        i = 0
        while i < self.N:
            x = np.random.uniform(left, right)
            y = np.random.uniform(down, up)

            p = geom.Point(x, y)

            z = np.random.uniform(0.0, 1.0)
            if z <= self.density(x, y) and p.within(self.polygon):
                particle_coords.append([x, y])
                i += 1


particle_coords = []
rho = ParticlesGenerator(20000, 300/1200, 650/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 500/1200, 775/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 0.8, 0.8, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 850/1200, 250/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 640/1200, 1150/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 150/1200, 1100/1200, [30, 30])
rho.points_generator()

x_array = np.array(particle_coords)[:, 0]
y_array = np.array(particle_coords)[:, 1]

########################################################
float_type = np.float64
int_type = np.int32

box_size = 1

m_0 = 2*1.6735575e-24 # масса молекулы водорода в граммах
n_0 = 2*10**5 # характерная концентрация частиц в частицах на куб. см

m_unit = 2*10**33 # единица массы (солнечная масса)
len_unit = 9.460e17 # единица длины (1 парсек)
vel_unit = 100 # единица скорости (1 м/с)

len_nebulas_x = 1
len_nebulas_y = 1
square_nebulas = len_nebulas_x * len_nebulas_y / len(x_array)

scale_0 = 0.1 * len_unit # характерная толщина туманности
rho_gass_in_square = m_0 * n_0 * scale_0
gas_mass = rho_gass_in_square * square_nebulas

gas_part_num = len(x_array)
gas_coords = np.zeros([gas_part_num, 3], dtype=float_type)
gas_vel = np.zeros([gas_part_num, 3], dtype=float_type)
gas_masses = np.zeros(gas_part_num, dtype=float_type)

for i in range(len(x_array)):
    gas_coords[i, 0] = x_array[i]
    gas_coords[i, 1] = y_array[i]

    gas_vel[i, 0] = float_type(x_array[i]/np.sqrt(x_array[i]**2 + y_array[i]**2) * 300000)
    gas_vel[i, 1] = float_type(y_array[i]/np.sqrt(x_array[i]**2 + y_array[i]**2) * 300000)
    
    gas_masses[i] = gas_mass 


##############################################
background_parts = 500

m_bg = 2*1.6735575e-24 # масса молекулы вакуума
n_bg = 2*10**1 # характерная концентрация частиц в вакууме

square_bg = box_size**2 / background_parts

scale_0 = 0.1 * len_unit # характерная толщина туманности
rho_bg_in_square = m_bg * n_bg * scale_0
bg_mass = rho_bg_in_square * square_bg

bg_coords = np.zeros([background_parts, 3], dtype=float_type)
bg_velocity = np.zeros([background_parts, 3], dtype=float_type)
bg_masses =  np.zeros(background_parts, dtype=float_type)

for i in range(background_parts):
    bg_coords[i, 0] = float_type(random.uniform(0, box_size))
    bg_coords[i, 1] = float_type(random.uniform(0, box_size))

    bg_masses[i] = bg_mass

all_parts = gas_part_num + background_parts
all_coords = np.zeros([all_parts, 3], dtype=float_type)
all_velocity = np.zeros([all_parts, 3], dtype=float_type)

for i in range(all_parts):
    if i < gas_part_num:
        all_coords[i, :] = gas_coords[i, :]
        all_velocity[i, :] = gas_vel[i, :]
    else:
        all_coords[i, :] = bg_coords[i-gas_part_num, :]
        all_velocity[i, :] = bg_velocity[i-gas_part_num, :]

all_mass = np.append(gas_masses, bg_mass)


##############################################
IC = h5py.File('./CrabNebula.hdf5', 'w')
header = IC.create_group("Header") 
part0 = IC.create_group("PartType0")

KEY_STUB = 0
KEY_STUB_ARRAY = np.ones(6, dtype = int_type)
num_part = np.array([all_parts, 0, 0, 0, 0, 0], dtype=int_type)
header.attrs.create("NumPart_ThisFile", num_part)
header.attrs.create("NumPart_Total_HighWord", np.zeros(6, dtype=int_type))
header.attrs.create("NumPart_Total", num_part)
header.attrs.create("MassTable", KEY_STUB_ARRAY)
header.attrs.create("Time", KEY_STUB)
header.attrs.create("BoxSize", box_size)
header.attrs.create("Redshift", KEY_STUB)
header.attrs.create("Omega0", KEY_STUB)
header.attrs.create("OmegaB", KEY_STUB)
header.attrs.create("OmegaLambda", KEY_STUB)
header.attrs.create("HubbleParam", KEY_STUB)
header.attrs.create("Flag_Sfr", KEY_STUB)
header.attrs.create("Flag_Cooling", KEY_STUB)
header.attrs.create("Flag_StellarAge", KEY_STUB)
header.attrs.create("Flag_Metals", KEY_STUB)
header.attrs.create("Flag_Feedback", KEY_STUB)
header.attrs.create("NumFilesPerSnapshot", KEY_STUB)
header.attrs.create("Flag_DoublePrecision", 1)

part0.create_dataset("ParticleIDs", data=np.arange(0, all_parts))
part0.create_dataset("Coordinates", data=all_coords)
part0.create_dataset("Velocities", data=all_velocity)
part0.create_dataset("Masses", data=all_mass)

IC.close()
