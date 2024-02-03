from flask import Flask, render_template, request
import openai
app = Flask(__name__, template_folder ="templates")
openai.api_key  = "<place your openai_api_key>"


@app.route("/")
def home():    
    return render_template("chatbotpage.html")

@app.route("/get")
def get_bot_response():    
    userText = "kwsg"
    response = "k"
    return response

if __name__ == "__main__":
    app.run()