from flask import Flask, render_template, request
app = Flask(__name__, template_folder ="templates")


@app.route("/")
def home():    
    return render_template("pdfread.html")

if __name__ == "__main__":
    app.run()