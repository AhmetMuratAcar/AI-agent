import os
from google.genai import types


# Schema for LLM
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory: str, directory: str = None) -> str:
    if not directory:
        directory = "."

    try:
        full_path = os.path.join(working_directory, directory)

        # Check validity of directory
        if not os.path.isdir(full_path):
            return f'Error: "{full_path}" is not a directory'

        # Is directory in working_directory
        abs_working_path = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        secure_check = abs_full_path.startswith(abs_working_path)

        # print(f"abs_working_path: {abs_working_path}\nabs_dir_path: {abs_full_path}\ncheck: {secure_check}")

        if not secure_check:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Build and return contents
        contents = os.listdir(abs_full_path)
        content_info = []

        for p in contents:
            res = "- " + p + ": file_size="
            curr_path = os.path.join(full_path, p)

            size = os.path.getsize(curr_path)
            res += str(size) + " bytes, is_dir="

            is_dir = os.path.isdir(curr_path)
            res += str(is_dir)
            content_info.append(res)

        formatted_res = "\n".join(content_info)
        return formatted_res

    except Exception as e:
        return f"Error: {str(e)}"
