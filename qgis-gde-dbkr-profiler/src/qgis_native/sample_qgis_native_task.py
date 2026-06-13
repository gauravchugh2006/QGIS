"""Mock a QGIS-like task until real QGIS API calls are plugged into the repo."""

def sample_qgis_native_task():
    """Transform sample layer names to imitate simple QGIS data processing."""
    layers = ["roads", "buildings", "parcels", "network"]
    return [layer.upper() for layer in layers]
