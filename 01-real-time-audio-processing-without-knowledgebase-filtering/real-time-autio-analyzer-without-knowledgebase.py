import os
import mysql.connector
from datetime import datetime
import speech_recognition as sr
from happytransformer import HappyTextClassification


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="without_knowledgebase_hate_speech_database"
)


happy_tc = HappyTextClassification("BERT", "Hate-speech-CNERG/dehatebert-mono-english")

speech_recognizer = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        speech_recognizer.pause_threshold = 1
        audio = speech_recognizer.listen(source, phrase_time_limit=10) # phrase_time_limit=10

        try:
            print("Recognizing...") 
            text = speech_recognizer.recognize_google(audio)
            return text

        except Exception as e:
	        print(e)


def hate_speech_classification(text):

	result = happy_tc.classify_text(text)

	now = datetime.now()
	currentTime = now.strftime("%I:%M:%S %p")
	currentDate = datetime.today().strftime('%Y-%m-%d')

	hate_words_list_str = ""

	text = text.replace("'","") # Replace ' with nothing to fix the issue.

	insert_cursor = mydb.cursor()
	sqlCode = "INSERT INTO processed_data VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format("", str(text) , currentDate, currentTime, result.label, (float(result.score) * 100))
	insert_cursor.execute(sqlCode)
	mydb.commit()

	print("Data inserted!")




def main_function():

    while True:
    	
    	text = speech_to_text()
    	
    	if text != "" and text != None:
    		hate_speech_classification(text)



if __name__ == "__main__": 
    main_function()