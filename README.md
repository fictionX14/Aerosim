# Aerosim

Aerosim is a Python-based simulation tool for modeling and visualizing basic aerospace flight dynamics. The project demonstrates the fundamentals of missile trajectory simulation, including guidance, navigation, and control (GNC) concepts.

## Features
- Simulates 2D missile flight under thrust and gravity
- Modular code structure for dynamics, control, and guidance
- Plots and saves the missile trajectory as an image
- Easily extensible for real-time control, guidance, and advanced visualization

## Requirements
- Python 3.12+
- matplotlib

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Activate your virtual environment (if using one):
   ```bash
   source venv/bin/activate
   ```
2. Run the simulation:
   ```bash
   python main.py
   ```
3. The trajectory will be saved as `trajectory.png` in the project directory.

## File Structure
- `main.py` — Main simulation script; sets parameters, runs the loop, and plots results
- `dynamics.py` — Contains the `update_state` function for physics calculations
- `requirements.txt` — Python dependencies

## Extending the Project
- Add new modules for guidance, navigation, or control algorithms
- Replace static parameters with user input or GUI controls
- Implement real-time or interactive visualization using Tkinter, PyQt, or web dashboards

## Example Output
![Missile Trajectory](trajectory.png)

## License
MIT License
