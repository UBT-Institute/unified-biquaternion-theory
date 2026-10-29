"""Component dimension and trial normalization arithmetic, not UBT mode selection."""
import sympy as s


def verify():
    basis = []
    for row in range(2):
        for column in range(2):
            matrix = s.zeros(2)
            matrix[row, column] = 1
            basis.append(matrix.reshape(4, 1))
    rank = s.Matrix.hstack(*basis).rank()
    assert rank == 4
    radius = s.symbols("radius", positive=True)
    trial_level = 8*s.pi*radius**2
    assert s.diff(trial_level, radius) != 0
    return {"complex_component_dimension": rank, "real_component_dimension": 2*rank,
            "physical_charged_mode_count": None, "selected_current_algebra_level": None}


if __name__ == "__main__":
    print(verify())
