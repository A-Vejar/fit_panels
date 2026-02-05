import math
from typing import Dict


# Input validation function
def valid_input(data: str) -> float:
    while True:
        try:
            value = float(input(data))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("¡It only can be input positive number!")


# Panels function
def fit_panels(roof: Dict[str, float], panel: Dict[str, float]) -> int:
    return math.floor(roof["width"] / panel["width"]) * math.floor(
        roof["height"] / panel["height"]
    )


# Leftovers function
def calculate_leftovers(
    roof: Dict[str, float], base: Dict[str, float], rotated: Dict[str, float]
) -> int:

    x_axis = math.floor(roof["width"] / base["width"])
    y_axis = math.floor(roof["height"] / base["height"])

    used_width = x_axis * base["width"]
    used_height = y_axis * base["height"]

    # Right strip
    right = fit_panels(
        {"width": (roof["width"] - used_width), "height": roof["height"]},
        {"width": rotated["width"], "height": rotated["height"]},
    )

    # Top strip
    top = fit_panels(
        {"width": used_width, "height": roof["height"] - used_height},
        {"width": rotated["width"], "height": rotated["height"]},
    )

    return right + top
