# dynamics.py
def update_state(MASS, GRAVITY, state, thrust, angle, dt):
    """
    state: [x, y, vx, vy]
    thrust: force in N
    angle: degrees from horizontal
    dt: timestep in seconds
    """
    from math import cos, sin, radians

    x, y, vx, vy = state
    ax = (thrust / MASS) * cos(radians(angle))
    ay = (thrust / MASS) * sin(radians(angle)) - GRAVITY

    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt

    return [x, y, vx, vy]
