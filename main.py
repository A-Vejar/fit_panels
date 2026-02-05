from utils import valid_input
from scripts import calculate_panels


# Main
def main() -> None:
    print("========================================================")
    # Roof dimensions
    print("Welcome, please type the 'ROOF' dimensions ...")
    X = valid_input("Width: ")
    Y = valid_input("Height: ")

    # Panels dimensions
    print("Please type the 'PANELS' dimensions ...")
    A = valid_input("Width: ")
    B = valid_input("Height: ")
    print("========================================================")

    result = calculate_panels(
        roof={"width": X, "height": Y}, panels={"width": A, "height": B}
    )
    print(f"*** It fits the amount of {result} panels")


if __name__ == "__main__":
    main()
