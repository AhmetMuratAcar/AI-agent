from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


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


def test_write_file():
    print("=== Testing write_file ===")
    test_cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),            # Expected: valid write
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),      # Expected: valid write
        ("calculator", "/tmp/temp.txt", "this should not be allowed")           # Expected: error
    ]

    for i, (working_dir, file_path, content) in enumerate(test_cases, 1):
        print(f"Test {i}: write_file({working_dir!r}, {file_path!r}, {content!r})")
        result = write_file(working_dir, file_path, content)
        print(result, "\n")


def test_run_python_file():
    print("=== Testing run_python_file ===")
    test_cases = [
        ("calculator", "main.py"),           # Expected: script runs successfully
        ("calculator", "tests.py"),          # Expected: script runs successfully
        ("calculator", "../main.py"),        # Expected: error (outside working directory)
        ("calculator", "nonexistent.py")     # Expected: error (file does not exist)
    ]

    for i, (working_dir, file_path) in enumerate(test_cases, 1):
        print(f"Test {i}: run_python_file({working_dir!r}, {file_path!r})")
        result = run_python_file(working_dir, file_path)
        print(result, "\n")


if __name__ == "__main__":
    test_get_files_info()
    test_get_file_content()
    test_write_file()
    test_run_python_file()
