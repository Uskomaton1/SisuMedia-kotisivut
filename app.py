from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/story")
def story():
    return render_template("story.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
