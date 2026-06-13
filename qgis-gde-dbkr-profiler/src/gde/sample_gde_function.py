"""Sample GDE workloads that stand in for real project code during setup."""

def sample_gde_frontend_workload(size: int = 50000) -> list[int]:
    """Simulate frontend-style list building so profiling can be tested safely."""
    return [i * 2 for i in range(size)]


def sample_gde_backend_workload(size: int = 100000) -> int:
    """Simulate backend-style computation with a heavier numeric workload."""
    return sum(i * i for i in range(size))
