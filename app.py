from flask import *
from cipher import playfair, affine, hill
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/playfair')
def playfair_page():
    return render_template("playfair.html")

@app.route('/playfair/encrypt')
def playfair_encrypt():
    plain = request.args.get("text")
    key = request.args.get("key")
    return playfair.encrypt(plain, key)

@app.route('/playfair/decrypt')
def playfair_decrypt():
    cipher = request.args.get("text")
    key = request.args.get("key")
    return playfair.decrypt(cipher, key)


@app.route('/vigenere', methods=["GET", "POST"])
def vigenere_page():
    if request.method == "POST":
        if request.form["vigenere_mode"] == "simpleVigenere":
            return redirect("/vigenere/simple")
        elif request.form["vigenere_mode"] == "autoKeyVigenere":
            return redirect("/vigenere/autokey")
        elif request.form["vigenere_mode"] == "fullVigenere":
            return redirect("/vigenere/full")
        elif request.form["vigenere_mode"] == "extendedVigenere":
            return redirect("/vigenere/extended")
    return render_template("vigenere.html")

@app.route('/vigenere/simple')
def simple_vigenere_page():
    return render_template("simple_vigenere.html")

@app.route('/vigenere/autokey')
def auto_key_vigenere_page():
    return render_template("auto_key_vigenere.html")

@app.route('/vigenere/full')
def full_vigenere_page():
    return render_template("full_vigenere.html")

@app.route('/vigenere/extended')
def extended_vigenere_page():
    return render_template("extended_vigenere.html")


@app.route('/affine')
def affine_page():
    return render_template("affine.html")

@app.route('/affine/encrypt')
def affine_encrypt():
    plain = request.args.get("text")
    m = int(request.args.get("keyM"))
    b = int(request.args.get("keyB"))
    return affine.encrypt(plain, m, b)

@app.route('/affine/decrypt')
def affine_decrypt():
    cipher = request.args.get("text")
    m = int(request.args.get("keyM"))
    b = int(request.args.get("keyB"))
    return affine.decrypt(cipher, m, b)


@app.route('/hill')
def hill_page():
    return render_template("hill.html")

@app.route("/hill/keycheck", methods = ["POST"])
def hill_check():
    key = request.form.get("key")
    key = json.loads(key)
    size = int(request.form.get("size"))
    keymat = [[int(key[i*size+j]) for j in range(size)] for i in range(size)]
    if hill.keycheck(keymat) :
        return "ok"
    return "Not ok"

@app.route("/hill/encrypt", methods=["POST"])
def hill_encrypt():
    plain = request.form.get("text")
    size = int(request.form.get("size"))
    key = request.form.get("key")
    key = json.loads(key)
    keymat = [[int(key[i*size+j]) for j in range(size)] for i in range(size)]
    return hill.encrypt(plain, keymat)

@app.route("/hill/decrypt", methods=["POST"])
def hill_decrypt():
    cipher = request.form.get("text")
    size = int(request.form.get("size"))
    key = request.form.get("key")
    key = json.loads(key)
    keymat = [[int(key[i*size+j]) for j in range(size)] for i in range(size)]
    return hill.decrypt(cipher, keymat)


@app.route('/upload/<cipher>', methods = ['GET', 'POST'])
def upload_file(cipher):
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f"{cipher}-input.txt"))
        f = open(f"{cipher}-input.txt")
        return render_template(f"{cipher}.html", fileContent=f.read())
    return home();


if __name__ == "__main__":
    app.run(debug=True)