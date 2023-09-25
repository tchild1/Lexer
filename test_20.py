import os
import project1
import sys
import pytest

@pytest.fixture
def bucket(request):
    return request.config.getoption("--bucket")

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read()

def test_project1(bucket):
    TEST_ROOT_DIR = "./project1-passoff/" + bucket
    test_filenames = [f for f in os.listdir(TEST_ROOT_DIR) if f.startswith("input")]
    passed = True
    for filename in test_filenames:
        input_file = os.path.join(TEST_ROOT_DIR, filename)
        input_contents = read_file_contents(input_file)

        answer_file = os.path.join(TEST_ROOT_DIR, filename.replace('input', 'answer'))
        answer_contents = read_file_contents(answer_file)
        try:
            assert project1.project1(input_contents) == answer_contents
            print("\n")
            print("Passed test: " + filename)
        except AssertionError as e:
            passed = False
            print("\n")
            print("Failed input: " + filename)
            print("--------------------------")
            print(e)
            print("--------------------------")
    assert passed

# input22 = """
# ,
#     .
# ?
#     (
# )
#     :::
# :-

# ,.?()::-"""

# answer22 = '''(COMMA,",",2)
# (PERIOD,".",3)
# (Q_MARK,"?",4)
# (LEFT_PAREN,"(",5)
# (RIGHT_PAREN,")",6)
# (COLON,":",7)
# (COLON,":",7)
# (COLON,":",7)
# (COLON_DASH,":-",8)
# (COMMA,",",10)
# (PERIOD,".",10)
# (Q_MARK,"?",10)
# (LEFT_PAREN,"(",10)
# (RIGHT_PAREN,")",10)
# (COLON,":",10)
# (COLON_DASH,":-",10)
# (EOF,"",12)
# Total Tokens = 17'''

# def test_project1():
#     assert project1.project1(input22) == answer22
