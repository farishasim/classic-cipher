from flask import *
import cipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/playfair')
def playfair_page():
    return render_template("playfair.html")

@app.route('/vigenere', methods=["GET", "POST"])
def vigenere_page():
    print("Hello")
    if request.method == "GET":
        try:
            mode = request.form["vMode"]
        except:
            mode = ""
        print("Mode:", mode)
    return render_template("vigenere.html", mode=mode)

if __name__ == "__main__":
    app.run(debug=True)