print("Simple Chatbot (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi!")
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user_input == "what is your name":
        print("Bot: I'm a simple chatbot.")
    elif user_input == "what can you do":
        print("Bot: I can chat with you and answer simple questions!")
    elif user_input == "who created you":
        print("Bot: I was created as a Python project.")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
