import os
import mysql.connector
from datetime import datetime
import speech_recognition as sr
from happytransformer import HappyTextClassification


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="the-project-aisle"
)


happy_tc = HappyTextClassification("BERT", "Hate-speech-CNERG/dehatebert-mono-english")

speech_recognizer = sr.Recognizer()

knowledgebase = []

def database_loader():

	with open('database/knowledgebase.txt') as f:
	  
	  for index, line in enumerate(f):
	    word = line.strip().lower()
	    knowledgebase.append(word)


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


def hate_speech_classification(text, hate_words):

	result = happy_tc.classify_text(text)

	now = datetime.now()
	currentTime = now.strftime("%I:%M:%S %p")
	currentDate = datetime.today().strftime('%Y-%m-%d')

	hate_words_list_str = ""

	for index, word in enumerate(hate_words):
		
		if index == 0:
			hate_words_list_str = hate_words_list_str + word
		else:
			hate_words_list_str = hate_words_list_str+" | " + word

	text = text.replace("'","") # Replace ' with nothing to fix the issue.

	insert_cursor = mydb.cursor()
	sqlCode = "INSERT INTO real_time_data VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format("", str(text), hate_words_list_str , currentDate, currentTime, result.label, result.score)
	insert_cursor.execute(sqlCode)
	mydb.commit()

	print("Data inserted!")



def hate_word_filtter(text):
	hate_words = []
	for word in knowledgebase:
		if word in text:
			hate_words.append(word)

	if len(hate_words) > 0:
		hate_speech_classification(text, hate_words)


def main_function():

    while True:
    	
    	text = speech_to_text()
    	
    	if text != "" and text != None:
    		hate_word_filtter(text)



if __name__ == "__main__": 
    database_loader()
    main_function()