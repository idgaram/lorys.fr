from flask import Flask, render_template

app = Flask(__name__, static_folder="static")
app.secret_key = "test"

@app.route("/")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)