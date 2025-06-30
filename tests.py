from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test_get_files_info():
    print("=== Testing get_files_info ===")
    test_cases = [
        ("calculator", "."),       # Expected: valid result
        ("calculator", "pkg"),     # Expected: valid result
        ("calculator", "/bin"),    # Expected: error string
        ("calculator", "../"),     # Expected: error string
        ("calculator", None)       # Expected: valid result
    ]

    for i, (working_dir, directory) in enumerate(test_cases, 1):
        print(f"Test {i}: get_files_info({working_dir!r}, {directory!r})")
        result = get_files_info(working_dir, directory)
        print(result, "\n")


def test_get_file_content():
    print("=== Testing get_file_content ===")
    test_cases = [
        ("calculator", "main.py"),               # Expected: valid result
        ("calculator", "pkg/calculator.py"),     # Expected: valid result
        ("calculator", "/bin/cat"),              # Expected: error or permission issue
        # ("calculator", "lorem.txt")              # Expected: valid truncated result
    ]

    for i, (working_dir, file_path) in enumerate(test_cases, 1):
        print(f"Test {i}: get_file_content({working_dir!r}, {file_path!r})")
        result = get_file_content(working_dir, file_path)
        print(result, "\n")


if __name__ == "__main__":
    test_get_files_info()
    test_get_file_content()
