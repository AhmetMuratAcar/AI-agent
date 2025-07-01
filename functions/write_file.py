import os
from google.genai import types


# Schema for LLM
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given contents to the given file path replacing previously existing content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file that will be written to. Relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written to the file at given file path.",
            ),
        },
    ),
)


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        full_path = os.path.join(working_directory, file_path)

        # Is file_path in working_directory
        abs_working_path = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        secure_check = abs_full_path.startswith(abs_working_path)

        if not secure_check:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # If file_path does not exist, create it
        dir_path = os.path.dirname(full_path)
        os.makedirs(dir_path, exist_ok=True)

        # Write content
        with open(full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
