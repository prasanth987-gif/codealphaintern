
def get_response(user_input):
    """Return a predefined reply based on matching keywords in user input."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm a simple rule-based chatbot built in Python."

    elif "help" in text:
        return "I can chat about basic things. Try saying hello, asking how I am, or saying bye."

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Could you rephrase it?"


def chat():
    print("=" * 50)
    print("Simple Chatbot (type 'bye' to exit)")
    print("=" * 50)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # End the loop after the chatbot says goodbye
        if user_input.lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
