import time

# defining the introduction function
def project_intro_bot():
    print("Hello, I am your project introduction bot!")
    time.sleep(3)
    print("I am here to introduce you to our project.")
    time.sleep(3)
    print("Our project is called ENGINEERING PROBLEMS AND UNIQUE TERMINOLOGY SOLUTIONS.")
    time.sleep(3)
    print("Our project deals with community engagement that involves people interacting with each other to resolve each other's doubts and help each other in various fields .")
    time.sleep(3)
    print("We hope that this project will help build a sense of community and encourage members to engage with each other on a regular basis,build trust, and deepen relationships.")
    time.sleep(3)
    print("Thank you for listening to our project introduction! For any further queries you can have a personal chat with us.")

    print("You can chat with our bot anytime for any personal queries below =>")
    
# calling function 
project_intro_bot()

# Define a function to handle the user's input
def handle_input(user_input):
    if user_input == 'hello':
        return 'Hi there! My name is Introbot. Our community helps people to talk things out , resolve issues, train people with their skills etc, Is there any way i can help you?'
    elif user_input == 'I need help with personality development':
        return 'Sure, we have various mentors here who can help you with your confidence, aptitude and all other grooming.'
    elif user_input == 'I need help with skill development':
        return 'Sure, we have technical experts with us who can help you with any kind of skills that lies in our domain.'
    else:
        return 'I am sorry, I did not understand that.'

# Loop to continue the conversation
while True:
    # Get input from the user
    user_input = input('User: ')

    # Process the user's input and get a response
    response = handle_input(user_input)
    # Display the bot's response to the user
    print('Bot: ' + response)

    # End the loop if the user says goodbye
    if user_input == 'goodbye':
        break

