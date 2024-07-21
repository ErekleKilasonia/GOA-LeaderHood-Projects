import json
from difflib import get_close_matches
import speech_recognition as sr
import pyttsx3



def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data : dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path,"w") as file:
        json.dump(data,file, indent=2)

def questions_best_match(user_question: str, questions: list):
    matches = get_close_matches(user_question,questions, n=1, cutoff=0.6)
    return matches[0] if matches != [] else None

def answer_for_question(question: str,knowledge_base: dict):
    for i in knowledge_base["questions"]:
        if i["question"] == question:
            return i["answer"]
        
def chatbot():
    knowledge_base : dict = load_knowledge_base('knowledge_base.json')
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    print("Which chatbot do you want woman or man?")
    text = "black"
    while True:
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            if text == "woman" or text == "women":
                print("Woman chatbot selected.")
                break
            elif text == "man" or text=="men" or text=="main":
                print("Man chatbot selected.")
                break
        except Exception as e:
            print("Try again")
    voices = engine.getProperty('voices') 
    if text == "woman" or text=="women":
        engine.setProperty('voice', voices[1].id)
    elif text == "man" or text=="men" or text=="main":
        engine.setProperty('voice', voices[0].id)
    while True:
        x = "Try again"
        while x == "Try again":
            with sr.Microphone() as source:
                audio_data = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio_data)
                print("You: " + text)
                x = "black"
            except Exception as e:
                x = "Try again"
                print(x)
        user_question: str = text
        if user_question.lower() == "quit" or user_question.lower() == "exit":
            break

        best_match: str | None = questions_best_match(user_question, [i["question"] for i in knowledge_base["questions"]])

        if best_match:
            answer = answer_for_question(best_match, knowledge_base) 
            engine.say(answer)
            engine.runAndWait()
            print(f"Bot: {answer}")
        else:
            engine.say("I don't know the answer. Can you teach me?")
            engine.runAndWait()
            print("Bot: I don't know the answer. Can you teach me? ")
            x = "Try again"
            while x == "Try again":
                with sr.Microphone() as source:
                    audio_data = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio_data)
                    print("You: " + text)
                    x = "black"
                except Exception as e:
                    x = "Try again"
                    print(x)
            new_answer = text
            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question":user_question,"answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                engine.say("Thank You I learned a new response!")
                engine.runAndWait()
                print("Bot: Thank You I learned a new response!")

chatbot()