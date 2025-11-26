# 1D Motion under Constant Force (Visualization)

This script simulates the one-dimensional motion of an object under a constant applied force and visualizes its position over time using Matplotlib.

It uses a simple numerical integration (Euler method) to update velocity and position at discrete time steps.

## Features

- Prompts for mass (kg) and constant force (N) at runtime
- Computes acceleration as `a = F / m`
- Integrates motion using a fixed `time_step` (Euler integration)
- Plots position vs. time over a configurable total duration

## Requirements

- Python 3.8+
- NumPy
- Matplotlib

## Installation

1. Ensure you have Python 3 installed.
2. Optionally create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

Run the script and follow the prompts:

```bash
python main.py
```

You will be asked:
- `Enter the mass of the object (in kg):` — e.g., `2.0`
- `Enter the constant force applied to the object (in N):` — e.g., `10.0`

After entering values, a plot window will display position vs. time.

### Key parameters

- `position`: Initial position (meters), default `0.0`
- `velocity`: Initial velocity (m/s), default `0.0`
- `mass`: User-provided mass (kg)
- `force`: User-provided constant force (N)
- `time_step`: Integration time step (seconds), default `0.01`
- `total_time`: Simulation duration (seconds), default `10.0`

## Physics Background

Under a constant force `F`, acceleration is constant:

- `a = F / m`
- Velocity evolves as `v(t) = v0 + a t`
- Position evolves as `x(t) = x0 + v0 t + 0.5 a t^2`

This script uses discrete updates (Euler method):
- `v_{n+1} = v_n + a * dt`
- `x_{n+1} = x_n + v_{n+1} * dt`

Note: Euler integration is simple but introduces numerical error. For better accuracy, consider semi-implicit (symplectic) Euler or higher-order methods.

## Customization

- Change `time_step` or `total_time` to refine resolution or duration.
- Set non-zero initial `position` or `velocity` to explore different initial conditions.
- Plot velocity alongside position:
  ```python
  plt.plot(times, velocities, label='Velocity (m/s)')
  plt.legend()
  ```

## Troubleshooting

- If the plot window doesn’t appear, ensure you are running in an environment that supports GUI windows (e.g., local machine, not a headless server). On headless systems, use:
  ```python
  import matplotlib
  matplotlib.use('Agg')  # before importing pyplot
  ```
  and save the figure instead of `plt.show()`:
  ```python
  plt.savefig('position.png', dpi=150)
  ```
- If you get `ImportError` for NumPy or Matplotlib, reinstall:
  ```bash
  pip install --upgrade numpy matplotlib
  ```

## License

This project is provided as-is for educational purposes. Add a license (e.g., MIT) if you plan to distribute or reuse.