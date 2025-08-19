# guidance.py - This file will contain the guidance logic for the Aerosim simulation.

# This module will handle the pitch and yaw guidance for the missile.
# for now, we will keep it simple and just use a fixed angle.

import numpy as np
import config as cfg

def pitch_angle_rad(t: float) -> float:

    return np.radians(cfg.ANGLE)

"""def yaw_angle_rad(t: float) -> float:
    # For now, we will keep yaw constant at 0 degrees
    return 0.0"""