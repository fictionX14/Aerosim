# dynamics.py  -- 2D point-mass with constant gravity and thrust
import numpy as np
import config as cfg
from control import thrust_vector

# State vector = [x, y, vx, vy] in SI units

def eom(t: float, y: np.ndarray) -> np.ndarray:
    """
    Equations of motion (flat-Earth gravity downward).
    y = [x, y, vx, vy]
    """
    x, y_pos, vx, vy = y
    v = np.array([vx, vy])

    # Forces
    T = thrust_vector(t)                  # N
    W = np.array([0.0, -cfg.GRAVITY]) * cfg.MASS  # N

    # Acceleration
    a = (T + W) / cfg.MASS

    # State derivative
    dy = np.array([vx, vy, a[0], a[1]])
    return dy

def rk4_step(fun, t, y, dt):
    """Classic RK4 integrator step."""
    k1 = fun(t, y)
    k2 = fun(t + 0.5*dt, y + 0.5*dt*k1)
    k3 = fun(t + 0.5*dt, y + 0.5*dt*k2)
    k4 = fun(t + dt,     y + dt*k3)
    return y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

