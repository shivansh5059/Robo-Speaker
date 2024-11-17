import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. Created by Tyagi")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to Speak (or type 'q' to quit): ")
        if x.lower() == "q":
            print("Goodbye!")
            break
        # Use the text-to-speech engine to speak the input
        engine.say(x)
        engine.runAndWait()