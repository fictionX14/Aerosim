# config.py - baeline for now, considering flat Earth gravity

# Simulation parameters will all be in SI units for consistency


MASS = 12500.0  # kg
GRAVITY = 9.81  # m/s^2
TIME_STEP = 0.5  # seconds
SIM_TIME = 180.0  # seconds
THRUST = 200000.0  # N
ANGLE = 45.0  # degrees (will be converted to radians in guidance.py) 
# from horizontal, will change in future to allow for variable angle
# in the future, we might want to allow for variable thrust and angle
# or even a more complex control system

#to keep track of plotting and output,we will record data points in a .csv
PLOT = True
CSV_OUT = "ascent.csv" # for timeseries output
# this will be used to save the trajectory data for further analysis
# in the future, we might want to add more parameters or change the output format
