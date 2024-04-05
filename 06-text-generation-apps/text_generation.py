import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API key is not set")

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.azure_endpoint = "https://ai4beg-luru.openai.azure.com/"


def invoke_completion():
    """Invokes an LLM for a simple completion"""
    prompt = """Complete the following: Once upon a time there was a"""
    completion = openai.completions.create(model="babbage-002", prompt=prompt)
    print(completion.choices[0].text)


def invoke_chat_completion():
    """Invokes a chat completion model"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is your name?"},
    ]
    completion = openai.chat.completions.create(
        model="text-generation-gpt35", messages=messages
    )
    print(completion.choices[0].message.content)


def exec_chat():
    """Starts a chat with the chat completion model"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    print("Starting chat.  Type 'exit' to quit...\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        messages.append({"role": "user", "content": user_input})
        completion = openai.chat.completions.create(
            model="text-generation-gpt35", messages=messages
        )
        print("AI: ", completion.choices[0].message.content)
        messages.append(
            {"role": "assistant", "content": completion.choices[0].message.content}
        )


if __name__ == "__main__":
    choice = ""
    while choice != "4":
        choice = input(
            "Enter 1 for completion, 2 for chat completion, 3 to chat, 4 to quit: "
        )
        if choice == "1":
            invoke_completion()
        elif choice == "2":
            invoke_chat_completion()
        elif choice == "3":
            exec_chat()
