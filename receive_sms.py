import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	response = MessagingResponse()

	response.message("Your mother thanks you for remembering her.")

	return str(response)


if __name__ == '__main__':
	app.run(debug=True)	