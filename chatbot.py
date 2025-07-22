print("Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    if user_input in ['hi', 'hello']:
        print("Chatbot: Hello! How can I help you?")
    elif user_input == 'how are you':
        print("Chatbot: I'm doing well. Thank you!")
    elif user_input == 'what is your name':
        print("Chatbot: I'm a simple chatbot made by Spoorthy 😄")
    elif user_input == 'who created you':
        print("Chatbot: I was created by Spoorthy using Python ❤️")
    elif user_input == 'bye':
        print("Chatbot: Goodbye! Talk to you later 👋")
        break
    else:
        print("Chatbot: I'm still learning... Can you ask something else?")