import speech_recognition as sr

# Step 1: Recognizer ko initialize karte hain
recognizer = sr.Recognizer()  # Yeh recognizer ko setup karta hai jo speech ko text mein convert karega

# Step 2: Microphone se sunne ke liye, microphone ko use karte hain
with sr.Microphone() as source:  # 'source' microphone hai jahan se hum audio sunenge
    print("Please speak something...")  # User ko keh rahe hain ke kuch bolain
    
    # Step 3: Ambient noise (background noise) ko adjust karna
    recognizer.adjust_for_ambient_noise(source)  # Yeh background noise ko samajhne aur adjust karne ke liye hota hai
    
    # Step 4: User ki speech sunte hain
    audio = recognizer.listen(source)  # Yeh listen() method microphone se audio record karte hai

    try:
        # Step 5: Google ke speech recognition engine ka use kar ke audio ko text mein convert karte hain
        text = recognizer.recognize_google(audio)  # Google engine audio ko text mein convert karega
        print(f"You said: {text}")  # Yeh print karega ki user ne kya bola

    except sr.UnknownValueError:
        # Agar audio ko samajh nahi paaya, toh yeh error handle karega
        print("Sorry, I could not understand the audio.")  # Agar samajh nahi paaye, toh yeh message dikhayega

    except sr.RequestError:
        # Agar request mein koi issue ho, jaise network ka issue ho, toh yeh error handle karega
        print("Sorry, there was an issue with the speech recognition service.")  # Agar Google recognition service ko 
                                                               # access karne mein koi problem ho, toh yeh message aayega