from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="
    background:#111;
    color:white;
    text-align:center;
    font-family:Arial">

    <h1 style="color:#00ff99">
    🎮 متجر الألعاب
    </h1>

    <h2>لعبة التجربة</h2>

    <p>أفضل لعبة أندرويد</p>

    <a href="/download">
    <button style="
    padding:15px;
    background:#00ff99;
    border-radius:10px">
    تحميل اللعبة
    </button>
    </a>

    </body>
    </html>
    """

@app.route("/download")
def download():
    return send_file("game.apk", as_attachment=True)


app.run(host="0.0.0.0", port=5000)