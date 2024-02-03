from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def log():
    with open("static/pdfs/temp.txt") as f:
        content = f.read()
    return render_template('log.html', content=content)


if __name__ == '__main__':
    app.run()