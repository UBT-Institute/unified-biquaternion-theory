"""Dimensionless classical response comparator; the Theta/biology bridge is open.

Neither variable is a fundamental field. No quantum coherence or consciousness
observable is implemented. See README.en.md and status.json for assumptions.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np


@dataclass(frozen=True)
class Parameters:
    """Unit-inertia effective coordinates; all parameters are dimensionless."""

    omega_n: float = 1.0
    omega_z: float = 1.3
    gamma_n: float = 0.2
    gamma_z: float = 0.15
    coupling: float = 0.25

    def __post_init__(self) -> None:
        values = (self.omega_n, self.omega_z, self.gamma_n,
                  self.gamma_z, self.coupling)
        if not all(math.isfinite(value) for value in values):
            raise ValueError("parameters must be finite")
        if min(values[:4]) <= 0:
            raise ValueError("frequencies and damping must be strictly positive")
        scale = self.omega_n * self.omega_z
        if not math.isfinite(scale) or not math.isfinite(scale * scale):
            raise ValueError("frequency scale exceeds finite arithmetic range")
        if abs(self.coupling) >= scale:
            raise ValueError("strict stability requires |coupling| < omega_n*omega_z")

    def stiffness(self) -> np.ndarray:
        return np.array([[self.omega_n**2, -self.coupling],
                         [-self.coupling, self.omega_z**2]], dtype=float)

    def drift(self) -> np.ndarray:
        """First-order matrix for (x, z, x_prime, z_prime)."""
        matrix = np.zeros((4, 4), dtype=float)
        matrix[:2, 2:] = np.eye(2)
        matrix[2:, :2] = -self.stiffness()
        matrix[2:, 2:] = -np.diag([self.gamma_n, self.gamma_z])
        return matrix

    def susceptibility(self, omega: float) -> np.ndarray:
        """Responses (x, z) to unit force on x, with exp(-i*omega*s)."""
        if not math.isfinite(omega):
            raise ValueError("drive frequency must be finite")
        denominator_n = self.omega_n**2 - omega**2 - 1j*self.gamma_n*omega
        denominator_z = self.omega_z**2 - omega**2 - 1j*self.gamma_z*omega
        determinant = denominator_n*denominator_z - self.coupling**2
        return np.array([denominator_z, self.coupling], dtype=complex) / determinant

    def energy(self, states: np.ndarray) -> np.ndarray:
        """H/E0 for a state or an array whose last axis has length four."""
        states = np.asarray(states, dtype=float)
        positions, velocities = states[..., :2], states[..., 2:]
        return (np.sum(velocities**2, axis=-1)
                + np.einsum("...i,ij,...j->...", positions,
                            self.stiffness(), positions)) / 2


def simulate(parameters: Parameters, times: np.ndarray, initial=None,
             drive_frequency: float = 0.0, drive_amplitude: float = 0.0):
    """Integrate the time-domain comparator; times use s=t/t0, not seconds."""
    from scipy.integrate import solve_ivp

    times = np.asarray(times, dtype=float)
    if (times.ndim != 1 or len(times) < 2 or not np.all(np.isfinite(times))
            or np.any(np.diff(times) <= 0)):
        raise ValueError("times must be a finite, strictly increasing vector")
    initial = np.zeros(4) if initial is None else np.asarray(initial, dtype=float)
    if initial.shape != (4,) or not np.all(np.isfinite(initial)):
        raise ValueError("initial state must have four finite components")
    if not math.isfinite(drive_frequency) or not math.isfinite(drive_amplitude):
        raise ValueError("drive parameters must be finite")
    matrix = parameters.drift()

    def rhs(time, state):
        derivative = matrix @ state
        derivative[2] += drive_amplitude * math.cos(drive_frequency*time)
        return derivative

    result = solve_ivp(rhs, (times[0], times[-1]), initial, t_eval=times,
                       method="DOP853", rtol=2e-10, atol=2e-12)
    if not result.success:
        raise RuntimeError(result.message)
    return result.y.T
