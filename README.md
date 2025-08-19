# This is Aerosim

 Aerosim is a Python-based tool for simulating and visualizing basic rocket ascent flight dynamics. It starts with a clean 2-D point-mass model and a modular layout (guidance, control, dynamics, navigation) that you can extend toward 3-D and advanced GNC.

# Features (current)

2-D ascent under thrust & gravity

Pitch program (constant for now); yaw parameter kept for future 3-D (ignored in 2-D math)

Propellant depletion via Isp and quadratic drag with a simple exponential atmosphere

RK4 integrator; plots Altitude, Speed, and Mass

Optional CSV export of the full time series

# Requirements

Python 3.12+

numpy, matplotlib

# Install:

pip install -r requirements.txt

# Quick start (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

python main.py


You’ll see plots for altitude, speed, and mass.
To export a CSV, set CSV_OUT = "ascent.csv" in config.py.

# Configuration

Edit config.py to change runtime, environment, vehicle, and guidance parameters:

# Integrator / runtime 
TIME_STEP = 0.1    # s
SIM_TIME  = 180.0  # s
PLOT      = True
CSV_OUT   = "ascent.csv" to export timeseries

# Environment (flat-Earth baseline)
G0 = 9.80665       # m/s^2 downward
RHO0 = 1.225       # kg/m^3 at sea level
H_SCALE_M = 8500.0 # m (exponential atmosphere scale height)

# Vehicle (single stage)
DRY_MASS_KG  = 1000.0
PROP_MASS_KG = 9000.0
THRUST_N     = 200000.0
ISP_S        = 300.0
CD           = 0.30
AREA_REF_M2  = 1.5

# Guidance (2-D) 
PITCH_DEG = 45.0   # elevation from horizontal (+up)
YAW_DEG   = 0.0    # placeholder for future 3-D; ignored in 2-D math

# File structure

main.py — runs the simulation; plotting and optional CSV output

dynamics.py — equations of motion (thrust, gravity, drag, mass burn) + RK4 step

control.py — computes thrust vector from guidance (keeps yaw param for future)

guidance.py — pitch/yaw schedule (currently constant; yaw parked)

navigation.py — derived quantities (e.g., altitude, speed)

config.py — editable parameters

requirements.txt, .gitignore, README.md

Roadmap

Multi-stage timeline & events

Guidance modes: gravity turn, pitch-kick, q/α limits

Atmosphere & aero fidelity (1976 Std Atmosphere, Cd(M))

3-D states with active yaw; Earth-fixed ↔ inertial framing

Monte-Carlo dispersions and summary dashboards

Optional C++ core (pybind11) with the same interfaces

# License

MIT License