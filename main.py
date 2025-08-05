# main.py

from dynamics import update_state
import matplotlib.pyplot as plt

#Constants

MASS = 1.0  # kg
GRAVITY = 9.81  # m/s^2 
TIME_STEP = 0.1  # seconds
SIM_TIME = 10.0  # seconds


state = [0.0, 0.0, 0.0, 0.0]
thrust = 20.0  # N
angle = 45.0  # degrees

# Logging data for plotting
trajectory = []

# Simulation Loop
time = 0.0
while time <= SIM_TIME:
    trajectory.append((time, *state))
    state = update_state(state, thrust, angle, TIME_STEP)
    time += TIME_STEP

# Plotting the trajectory
xvals = [pos[1] for pos in trajectory]
yvals = [pos[2] for pos in trajectory]

plt.plot(xvals, yvals)
plt.title('Missle Trajectory')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid(True)
plt.show()
