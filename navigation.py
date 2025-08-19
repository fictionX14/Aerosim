# navigation.py  -- derived quantities & simple telemetry
import numpy as np

def speed(vx: float, vy: float) -> float:
    return float(np.hypot(vx, vy))

def altitude(y_pos: float) -> float:
    # Flat-Earth baseline: altitude is y
    return float(y_pos)
