import numpy as np 
import matplotlib.pyplot as plt

#Distance reading on a vernier caliper in mm
#Force reading from a spring scale in Newtons
water_distance = np.array([0, 6.68, 12.10, 18.24, 24.82, 28.88, 32.58, 37.00, 41.24, 45.40, 48.00, 50.82, 54.41])
water_force = np.array([0.032, 0.032, 0.036, 0.042, 0.048, 0.052, 0.055, 0.058, 0.061, 0.063, 0.066, 0.067, 0.043])

soap_distance = np.array([0, 6.68, 12.10, 18.24, 24.82, 28.88, 32.58, 37.00, 41.24, 45.40, 48.00, 50.82, 54.41])
soap_force = np.array ([0.032, 0.032, 0.036, 0.042, 0.046, 0.049, 0.051, 0.053, 0.055, 0.059, 0.059, 0.043, 0])

water_slope = (water_force/water_distance*1.0)
soap_slope = (soap_force/soap_distance*1.0)

print(water_slope)
print(soap_slope)

plt.plot(water_distance, water_force , 'bo')
plt.plot(soap_distance, soap_force , 'ro')
#plt.legend(water_force, soap_force, loc = 'upper left')
plt.show()