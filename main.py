from flask import Flask, render_template, request ,jsonify
import pandas as pd

from llama_index import StorageContext, load_index_from_storage

import os

# Read the CSV file
df = pd.read_csv('topics.csv')

app = Flask(__name__, template_folder='templates')

os.environ["OPENAI_API_KEY"] = "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"
storage_context = StorageContext.from_defaults(persist_dir="chatbot/storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()


class Topic:      
    def __init__(self, id, topic, pdfdir, img, desc, phet):
        self.id = id
        self.topic = topic
        self.pdfdir = pdfdir
        self.img = img
        self.desc = desc
        self.phet = phet

def getTopics():
    listTopics = []
    for i in range(len(df)):
        row = df.iloc[i]
        topic = Topic(row['id'], row['topic'], row['pdfdir'], row['img'], row["desc"], row["phet"])
        listTopics.append(topic)
    return listTopics

@app.route('/')
def index():
    listOfTopics = getTopics()
    return render_template('index.html', items=listOfTopics)

@app.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    topic = next((t for t in getTopics() if t.id == topic_id), None)
    if topic:
        return render_template('topic_detail.html', item=topic)
    else:
        return "Topic page not found", 404

@app.route("/get")
def get_bot_response():
    # Retrieve the user's text from query parameters
    os.environ["OPENAI_API_KEY"] = "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"
    topic = next((t for t in getTopics() if t.id == int(request.args.get("topic_id"))), None)
    userText = "You are a chatbot for a learning website. Only answer what the user explicitly asks. Especially don't talk about the lab if the user doesn't mention the lab. The user will ask questions about various topics and this is the current topic: " + topic.topic
    userText = userText + " This is the user's query: " + request.args.get('msg')
    print(userText)
    
    # Placeholder for where you would process the userText to generate a response
    response = query_engine.query(userText).response
    
    return response

def process_user_input(userText):
    # Here, implement the logic to generate a response based on userText
    # This is a placeholder function. Replace it with your chatbot's logic.
    # For now, it simply echoes back the user's message
    return f"Echo: {userText}"


@app.route('/topic/phet/<int:topic_id>')
def phet_detail(topic_id):
    print("hello")
    topic = next((t for t in getTopics() if t.id == topic_id), None)
    
    if topic:
        return render_template('phet_detail.html', item=topic)
    else:
        return "Topic not found", 404

@app.route('/topic/pdf/<int:topic_id>')
def pdf_detail(topic_id):
    print("hello pdf")
    topic = next((t for t in getTopics() if t.id == topic_id), None)
    
    if topic:
        return render_template('pdf_detail.html', item=topic)
    else:
        return "Topic not found", 404

if __name__ == '__main__':
    app.run(debug=True)
