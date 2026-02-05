import json
from pathlib import Path
from typing import Dict, List
from scripts import calculate_panels


def run_tests() -> None:
    base_dir = Path(__file__).parent

    with open(base_dir / "test_cases.json", "r") as f:
        data = json.load(f)

    test_cases: List[Dict[str, int]] = [
        {
            "panels": {"width": test["panelW"], "height": test["panelH"]},
            "roof": {"width": test["roofW"], "height": test["roofH"]},
            "expected": test["expected"],
        }
        for test in data["testCases"]
    ]

    print("Running tests")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            roof=test["roof"],
            panels=test["panels"],
        )

        passed = result == test["expected"]

        print(f"Test {i}:")
        print(
            f"  Panels: {test['panels']['width']}x{test['panels']['height']}, "
            f"Roof: {test['roof']['width']}x{test['roof']['height']}"
        )
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


if __name__ == "__main__":
    run_tests()
