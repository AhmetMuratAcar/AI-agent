import os
from config import MAX_CHARS
from google.genai import types

# Schema for LLM
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the text contents inside of the given file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to get text content from, relative to the working directory.",
            ),
        },
    ),
)


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        full_path = os.path.join(working_directory, file_path)

        # Check validity of file path
        if not os.path.isfile(full_path):
            return f'Error: "{full_path}" is not a file'

        # Is file_path in working_directory
        abs_working_path = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        secure_check = abs_full_path.startswith(abs_working_path)

        if not secure_check:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Read and write file content
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: {str(e)}"
