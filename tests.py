from functions.get_files_info import get_files_info


def run_tests():
    test_cases = [
        ("calculator", "."),       # Expected: valid result
        ("calculator", "pkg"),     # Expected: valid result
        ("calculator", "/bin"),    # Expected: error string
        ("calculator", "../"),     # Expected: error string
    ]

    for i, (working_dir, directory) in enumerate(test_cases, 1):
        print(f"Test {i}: get_files_info({working_dir!r}, {directory!r})")
        result = get_files_info(working_dir, directory)
        print(result, "\n")


if __name__ == "__main__":
    run_tests()
