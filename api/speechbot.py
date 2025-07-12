from flask import Flask, render_template, jsonify, make_response
import speak

app = Flask(__name__)

@app.route('/greet')
def index():

	text1 = "hello! how can i help you"
	speak.tts(text=text1, lang="en")

	return text1


@app.route("/about")
def about():

	text2 = "Nice to meet you aditya"
	speak.tts(text=text2, lang="en")

	return text2


if __name__ == '__main__':

	app.run(debug = True)

