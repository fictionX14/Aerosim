# main.py  -- run the simulation
import numpy as np
import matplotlib.pyplot as plt
import csv
import config as cfg
from dynamics import eom, rk4_step
from navigation import speed, altitude

def run():
    dt = cfg.TIME_STEP
    steps = int(np.ceil(cfg.SIM_TIME / dt))

    # State: [x, y, vx, vy]
    y = np.array([0.0, 0.0, 0.0, 0.0], dtype=float)
    t = 0.0

    T = np.zeros(steps + 1)
    X = np.zeros(steps + 1)
    Y = np.zeros(steps + 1)
    VX = np.zeros(steps + 1)
    VY = np.zeros(steps + 1)
    ALT = np.zeros(steps + 1)
    SPD = np.zeros(steps + 1)

    # store initial
    T[0] = t; X[0], Y[0], VX[0], VY[0] = y
    ALT[0] = altitude(Y[0]); SPD[0] = speed(VX[0], VY[0])

    for k in range(1, steps + 1):
        y = rk4_step(eom, t, y, dt)
        t = k * dt

        T[k] = t
        X[k], Y[k], VX[k], VY[k] = y
        ALT[k] = altitude(Y[k]); SPD[k] = speed(VX[k], VY[k])

    print(f"Final t={T[-1]:.2f}s | alt={ALT[-1]:.2f} m | speed={SPD[-1]:.2f} m/s")

    if cfg.CSV_OUT:
        with open(cfg.CSV_OUT, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["t_s","x_m","y_m","vx_mps","vy_mps","alt_m","speed_mps"])
            for i in range(len(T)):
                w.writerow([T[i], X[i], Y[i], VX[i], VY[i], ALT[i], SPD[i]])
        print(f"Wrote {cfg.CSV_OUT}")

    if cfg.PLOT:
        plt.figure()
        plt.plot(T, ALT)
        plt.xlabel("Time (s)"); plt.ylabel("Altitude (m)"); plt.title("Altitude vs Time")

        plt.savefig('altitude.png')

        plt.figure()
        plt.plot(T, SPD)
        plt.xlabel("Time (s)"); plt.ylabel("Speed (m/s)"); plt.title("Speed vs Time")

        plt.savefig('trajectory.png')

if __name__ == "__main__":
    run()
