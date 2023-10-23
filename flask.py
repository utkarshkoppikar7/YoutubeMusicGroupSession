from flask import Flask, render_template

app = Flask(__name__)

@app.route("/getData")
def index():
    value = request.args.get("value")
    return render_template("index.html", value=value)

if __name__ == "__main__":
    app.run(debug=True)
