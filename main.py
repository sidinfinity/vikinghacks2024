from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

import re

def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url

# Replace 'your_file.csv' with the path to your CSV file

url ="https://docs.google.com/spreadsheets/d/1ULjkC6x--guX5A4veeJhEzCYuyuG0ryvJHseR9PWIOY/export?format=csv&gid={1ULjkC6x--guX5A4veeJhEzCYuyuG0ryvJHseR9PWIOY}"
new_url = convert_google_sheet_url(url)


# Read the CSV file
df = pd.read_csv(new_url)
print(df.head())
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