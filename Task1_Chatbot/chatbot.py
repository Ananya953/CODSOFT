def chatbot():
    print("CodBot: Hello! I am your chatbot. Ask me anything. (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("CodBot: Hello there! How can I assist you?")
        elif "your name" in user_input:
            print("CodBot: I'm CodBot, your AI assistant.")
        elif "internship" in user_input:
            print("CodBot: CodSoft offers internships in AI, Web Dev, Python, and more!")
        elif "thank you" in user_input:
            print("CodBot: You're welcome!")
        elif "bye" in user_input:
            print("CodBot: Goodbye! Have a great day ahead.")
            break
        else:
            print("CodBot: Sorry, I didn’t understand that.")

chatbot()