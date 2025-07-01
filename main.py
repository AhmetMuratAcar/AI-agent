import os
import sys
from typing import Dict

from config import MODEL, SYSTEM_PROMPT
from available_functions import available_functions
from functions.call_function import call_function

from dotenv import load_dotenv
from google import genai
from google.genai import types


def get_flag_map() -> Dict[str, bool]:
    flag_map = {
        "--verbose": False
    }

    return flag_map


def generage_content(client, messages, flags) -> genai.types.GenerateContentResponse:
    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT
        ),
    )

    # Flag checks
    if flags["--verbose"] is True:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

    # Calling functions
    if response.function_calls:
        for call in response.function_calls:
            func_res = call_function(
                function_call_part=call,
                verbose=flags["--verbose"]
            )

            if not func_res.parts[0].function_response.response:
                raise Exception("Error: no response from function")

            if flags["--verbose"] is True:
                print(f"-> {func_res.parts[0].function_response.response}")

    return response


def prep_sys() -> genai.Client:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    return client


def main():
    args = sys.argv[1:]
    if not args:
        print("ERROR: No prompt provided")
        print('USAGE: uv run main.py "your prompt" --flags')
        sys.exit(1)

    # Setting flags
    flags = get_flag_map()
    for arg in args[1:]:
        if arg in flags:
            flags[arg] = True

    # Creating user prompt
    user_prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # Flag checks
    if flags["--verbose"] is True:
        print(f"User prompt: {user_prompt}")

    # Conducting query
    client = prep_sys()
    response = generage_content(
        client=client,
        messages=messages,
        flags=flags,
    )
    print(response.text)


if __name__ == "__main__":
    main()
