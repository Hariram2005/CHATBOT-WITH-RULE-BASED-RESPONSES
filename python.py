import re

def simple_chatbot(user_input):
    # Predefined rules for the chatbot
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    questions = ["how are you", "what's up", "how's it going", "how do you do"]
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "default": "I'm not sure how to respond to that. Can you ask me something else?"
    }

    # Pattern matching using regular expressions
    if any(re.search(f'\\b{g}\\b', user_input, re.IGNORECASE) for g in greetings):
        return responses["hello"]
    elif any(re.search(f'\\b{q}\\b', user_input, re.IGNORECASE) for q in questions):
        return responses["how are you"]
    elif any(re.search(f'\\b{f}\\b', user_input, re.IGNORECASE) for f in farewells):
        return responses["bye"]
    else:
        return responses["default"]

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
