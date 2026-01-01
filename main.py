import datetime

name = input("Enter your name: ")
presentHour = datetime.datetime.now().hour
if 5 <= presentHour <= 11:
    print("Good Morning,", name)
elif 11 < presentHour <= 17:
    print("Good afternoon,", name)
elif 17 < presentHour <= 20:
    print("Good evening,", name)
else:
    print("Goodnight,", name)
print("Welcome to the Chatbot!")
print("You can ask me basic questions, type bye to exit from the bot")

# Make response keys lower-case for easy matching
responses = {
    "hello": "Hi, welcome, how may I help you?",
    "hi":"How are you?",
    "how are you?": "I am fine, thank you!",
    "who are you?": "I am smart AI Chatbot",
    "motivate me": "Keep going, every bug of your project makes you better developer!",
    "happy": "Glad to hear that",
    "functions kiya hote hain?": "Jakar chapter 7 parho"
}

# Function to get response of chatbot
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        # Match whole input or input containing a response phrase
        if userQuestion.strip() == eachkey or eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to tell that yet, Will learn soon"

# Take user inputs
while True:
    userInput = input("Please ask your question: ").strip().lower()
    if userInput == "bye":
        print("Bot response: Goodbye! Have a nice day.")
        break
    reply = getResponseBot(userInput)
    print("Bot response:", reply)