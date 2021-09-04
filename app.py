from flask import *
from cipher import playfair, affine, hill
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

if __name__ == "__main__":
    app.run(debug=True)