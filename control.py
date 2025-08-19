# control.py - This file contains the control logic for the simulation
# It will handle the control inputs for the rocket, such as thrust and angle adjustments.

import numpy as np
import config as cfg    
from guidance import pitch_angle_rad #, yaw_angle_rad

def thrust_vector(t: float) -> np.ndarray:
    
    thrust = pitch_angle_rad(t)
    # yaw = yaw_angle_rad(t)
    
    u = np.array([np.cos(thrust), np.sin(thrust)])
    # v = np.array([np.cos(yaw), np.sin(yaw)])

    return cfg.THRUST * u # may need to manipulate return value based on thrust and angle
