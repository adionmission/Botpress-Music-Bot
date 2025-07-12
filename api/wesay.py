import speech_recognition as sr
from flask import Flask, render_template, jsonify, make_response
import speak
from pygame import mixer
import time

app = Flask(__name__)
r = sr.Recognizer()


@app.route('/')
def index():

	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	text = r.recognize_google(audio)

	return text


@app.route('/intro')
def intro():

	textt = "Hello! how can i help you"
	speak.tts(text=textt, lang="en")

	return textt


@app.route('/play')
def play():

	text1 = "Playing the Jawaani song"
	speak.tts(text=text1, lang="en")

	mixer.init()
		
	mixer.music.load('C:/Users/Aditya/Desktop/extras/The Jawaani Song - SOTY 2.mp3')
		
	mixer.music.play()

	return text1


@app.route('/speakstop')
def speakstop():

	with sr.Microphone() as source:
		
		speak.tts(text="Anything else", lang="en")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	text = r.recognize_sphinx(audio)

	return text


@app.route('/stop')
def stop():

	text2 = "Ok, music stopped"
	speak.tts(text=text2, lang="en")

	mixer.init()
		
	mixer.music.pause()

	return text2


if __name__ == '__main__':

    app.run(debug = True)

