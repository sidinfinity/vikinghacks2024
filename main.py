from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from decimal import Decimal
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import DECIMAL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    name = "product100"
    print(name)
    #listOfItems= getLatestProducts()
    
    
    
    return render_template('index.html', )



if __name__ == '__main__':
    app.run(debug=True)