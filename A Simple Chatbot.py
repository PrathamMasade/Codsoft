#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
import pyjokes
def simple_chatbot(user_input):
    # Convert user input to lowercase in case of case-mismatch
    user_input = user_input.lower()

    # We Define some predefined rules and responses
    greetings = ["hello", "hi", "hey", "greetings","good morning!", "good afternoon!", "good evening!","good night!"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    questions = ["how are you?", "what's up?", "how do you do?", "what is the time?", "tell me a joke"]
    compliments = ["good job", "well done", "great job", "nice work", "thank you"]

    # Check user input against predefined rules
    if user_input in greetings:
        if user_input in "good morning!":
            return "Good Morning!"
        elif user_input in "good afternoon!":
            return "Good Afternoon!"
        elif user_input in "good evening!":
            return "Good Evening!"
        elif user_input in "good night!":
            return "Good Night!"
        else:
            return "Hello! How can I assist you today?" 

    elif user_input in farewells:
        return "Goodbye! Have a nice day!"

    elif user_input in questions:
        if "what is the time?" in str(user_input):
            current_time = datetime.now().strftime("%H:%M:%S")
            return "The time is: " + current_time
        elif "tell me a joke" in str(user_input):
            s= pyjokes.get_joke()
            return s
        else:
            return "I'm good, but thanks for asking!"

    elif user_input in compliments:
        if user_input=="thank you":
            return "You're Welcome!"
        else:
            return "Thank you! I appreciate your kind words."
    else:
        return "I'm not sure how to answer that. Can you ask something else?"

# Simple interactive loop
name = input("Please enter your name:")
c=input("What would you like to call me? ")
print("Hello "+name+"! Please type \"exit\" to stop talking to",c+".")
while True:  
    user_input = input(name+": ")
    if user_input.lower() == 'exit':
        print(c+": Goodbye!")
        break
    response = simple_chatbot(user_input)
    print(c+":", response)
    if "tell me a joke" in user_input.lower():
        while True:
            one_more=input(c+": Do you want to hear one more? ")
            if one_more.lower()=="no":
                print(c+": Hope it made you laugh!")
                break
            elif one_more.lower()=="yes":
                print(c+": Sure here's another one...")
                print(pyjokes.get_joke())


# In[ ]:




