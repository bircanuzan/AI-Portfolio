"""Reproducible CPU-only NumPy/SciPy regression exercise.

Dependencies: numpy, scipy.
"""
import json
import numpy as np
from scipy.optimize import least_squares

SEED = 42


def main():
    rng = np.random.default_rng(SEED)
    x = np.linspace(-2.0, 2.0, 120)
    noise = rng.normal(0, 0.15, size=x.shape)
    y = 1.8 * x - 0.7 + noise

    design = np.column_stack((x, np.ones_like(x)))
    numpy_parameters, *_ = np.linalg.lstsq(design, y, rcond=None)
    scipy_result = least_squares(
        lambda parameters: design @ parameters - y,
        x0=np.array([0.0, 0.0]),
    )
    summary = {
        "data": "synthetic",
        "seed": SEED,
        "rows": int(len(x)),
        "numpy_coefficients": numpy_parameters.tolist(),
        "scipy_coefficients": scipy_result.x.tolist(),
        "numpy_mse": float(np.mean((design @ numpy_parameters - y) ** 2)),
        "scipy_mse": float(np.mean((design @ scipy_result.x - y) ** 2)),
        "scipy_success": bool(scipy_result.success),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
