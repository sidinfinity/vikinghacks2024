from flask import Flask, render_template
import pandas as pd

# Read the CSV file
df = pd.read_csv('topics.csv')

app = Flask(__name__, template_folder='templates')

class Topic:      
    def __init__(self, id, topic, pdfdir, img):
        self.id = id
        self.topic = topic
        self.pdfdir = pdfdir
        self.img = img

def getTopics():
    listTopics = []
    for i in range(len(df)):
        row = df.iloc[i]
        topic = Topic(row['id'], row['topic'], row['pdfdir'], row['img'])
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
        return "Topic not found", 404

if __name__ == '__main__':
    app.run(debug=True)
