import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args=None) -> str:
    full_path = os.path.join(working_directory, file_path)

    # Check validity of file path
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    # Is file_path in working_directory
    abs_working_path = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
    secure_check = abs_full_path.startswith(abs_working_path)

    if not secure_check:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Is the given file a python file
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    # Run the script and construct res string
    try:
        commands = ["python3", abs_full_path]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            text=True,
            timeout=30,
            capture_output=True,
            cwd=abs_working_path
        )

        formatted_result = ""

        if not result.stderr and not result.stdout:
            formatted_result += "No output produced."
            return formatted_result
        else:
            formatted_result += f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\n"

        if result.returncode != 0:
            formatted_result += f"Process exited with code {result.returncode}"

        return formatted_result

    except Exception as e:
        return f"Error: executing Python file: {e}"
