from main import *

run_cases = [
    ((0, 1, 4, 2), 0, 1, 4, 2),
    ((5, 5, 0, 0), 5, 5, 0, 0),
]

submit_cases = run_cases + [
    ((-10, -10, -5, -5), -10, -10, -5, -5),
]


def test(input_args, expected_x1, expected_y1, expected_x2, expected_y2):
    try:
        print("---------------------------------")
        print(f"Input arguments: {input_args}")
        print("")

        # Create rectangle from input arguments
        rectangle = Rectangle(*input_args)

        print(f"Expected x1: {expected_x1}")
        print(f"Actual   x1: {rectangle.x1}")
        print(f"Expected y1: {expected_y1}")
        print(f"Actual   y1: {rectangle.y1}")
        print(f"Expected x2: {expected_x2}")
        print(f"Actual   x2: {rectangle.x2}")
        print(f"Expected y2: {expected_y2}")
        print(f"Actual   y2: {rectangle.y2}")

        # Check if the rectangle has all expected values
        if (
            rectangle.x1 == expected_x1
            and rectangle.y1 == expected_y1
            and rectangle.x2 == expected_x2
            and rectangle.y2 == expected_y2
        ):
            return True

        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
