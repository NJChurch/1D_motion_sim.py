import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
position = 0.0  # Initial position (m)
velocity = 0.0  # Initial velocity (m/s)
mass = float(input("Enter the mass of the object (in kg): "))
force = float(input("Enter the constant force applied to the object (in N): "))

#solving for new values
acceleration = force / mass
time_step = 0.01  
total_time = 10.0
num_steps = int(total_time / time_step)
positions = []
velocities = []
times = []

for step in range(num_steps):
    velocity += acceleration * time_step
    position += velocity * time_step
    positions.append(position)
    velocities.append(velocity)
    times.append(step * time_step)

# Setting up the figure and axis
plt.figure(figsize=(10, 5))
plt.plot(times, positions, label='Position (m)')
plt.title('1D Motion under Constant Force')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')

plt.grid(True)
plt.show()



