# Simple Python LLM Terminal Interface

__Do not give this program to others for them to use! It does not have all the security and safety features that a production AI agent would have. It is for learning purposes only.__

It is currently hard coded to work in the `./calculator` directory. This is done as a security measure by manually setting the `working_directory` parameter of all function calls within `./functions/call_function.py`.

## Setup
- Clone this repository and install the dependencies

Setup using uv:
```sh
git clone https://github.com/AhmetMuratAcar/AI-agent.git
cd AI-agent
uv venv
source .venv/bin/activate
uv pip install -r uv.lock
```
- Create an account and an API key for [Google AI Studio](https://aistudio.google.com/) and add your API key to your local `.env`
```sh
touch .env
echo GEMINI_API_KEY={your API key} >> .env
```
At this point you should be able to run the agent. If you want to change the model, maximum iterations it can perform, the maximum read file char length, or the system prompt, you can do so in `./config.py`.

## Functions

The agent is currently limited to:
- Getting file info
- Reading file content
- Writing to file
- Running <u>PYTHON</u> scripts

```Python
def get_files_info(working_directory: str, directory: str = None) -> str:
    """
    - {file_name}: {file_size}={size} bytes, is_dir={bool}
    """

def get_file_content(working_directory: str, file_path: str) -> str:
    """
    Returns complete contents of given file, capped at MAX_CHARS
    """

def write_file(working_directory: str, file_path: str, content: str) -> str:
    """
    Destructive write, completely replaces file contents.
    Creates required directories and files.
    """

def run_python_file(working_directory: str, file_path: str, args=None) -> str:
    """
    STDOUT: {result.stdout}
    STDERR: {result.stderr}
    """

```

