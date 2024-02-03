from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'topics.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Accessing the data from the columns
ids = df['id']
topics = df['topic']
pdf_dirs = df['pdfdir']
imgs = df['img']

# If you want to print the data
print("IDs:", ids)
print("Topics:", topics)
print("PDF Directories:", pdf_dirs)
print("Images:", imgs)

app = Flask(__name__, template_folder='templates')

class Item():      
    def __init__(self, id, topic, pdfdir, img):
        self.id = id
        self.topic = topic
        self.pdfdir = pdfdir
        self.img = img

def getTopic(topic_id):
    listOfItems = products.query.all()
    
    for index in range(len(listOfItems)):
        objectItem = listOfItems[index]
        if objectItem.id == item_id:
            priceItem = getPrice(item_id)
            item = objectItem
            item.price = priceItem
    
    return item





#---------------------------------------------

@app.route('/')
def index():
    name = "product100"
    print(name)
    #listOfItems= getLatestProducts()
    
    
    
    return render_template('index.html', )


@app.route('/topic/<int:item_id>')
def topic_detail(topic_id):
    print("reached"+ str(item_id))
    item = getItem(item_id)
    return render_template('item_detail.html', item=item)



if __name__ == '__main__':
    app.run(debug=True)