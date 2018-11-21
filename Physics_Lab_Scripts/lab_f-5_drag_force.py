import math
import numpy as np
import matplotlib.pyplot as plt

#Want to plot Drag Force vs Velocity for the five balls
drag_bearings = np.array([25.5, 53.6, 120])
velocity = np.array([1.84, 3.86, 8.44])
 
log_drag = np.log(drag_bearings)
log_velocity = np.log(velocity)

plt.plot(log_velocity, log_drag, 'bo')
plt.show()