
from main import *

run_cases = [
    (["hello", "world"], "hello,world"),
    (["this", "list", "is", "so", "important"], "this,list,is,so,important"),
]

submit_cases = run_cases + [
    ([], ""),
    (["ford", "ferrari", "tesla"], "ford,ferrari,tesla"),
    (["musk", "satya", "cook", "bezos"], "musk,satya,cook,bezos"),
    (["dota", "sc2", "overwatch", "diablo", "mtg"], "dota,sc2,overwatch,diablo,mtg"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = join_strings(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
