from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home Page</title>
            <meta charset="utf-8">
        </head>

        <body>
            <p>Hello Flask!</p>
        <body>
    </html>
    '''

@app.route("/albums/<album_number>/<song_number>")
def albums(album_number, song_number):
    return "The {} album and {} song.".format(album_number, song_number)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
