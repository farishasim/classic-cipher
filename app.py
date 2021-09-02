from flask import *
import cipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/playfair')
def playfair_page():
    return render_template("playfair.html")

if __name__ == "__main__":
    app.run(debug=True)