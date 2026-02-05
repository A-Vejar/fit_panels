from typing import Dict
from utils import fit_panels, calculate_leftovers


# Main function
def calculate_panels(roof: Dict[str, float], panels: Dict[str, float]) -> int:
    rotated_panel = {"width": panels["height"], "height": panels["width"]}

    normal = fit_panels(roof, panels)
    rotated = fit_panels(roof, rotated_panel)

    leftover_normal = calculate_leftovers(roof, panels, rotated_panel)
    leftover_rotated = calculate_leftovers(roof, rotated_panel, panels)

    total_normal = normal + leftover_normal
    total_rotated = rotated + leftover_rotated

    return max(total_normal, total_rotated)
