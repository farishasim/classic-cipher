from flask import *
from cipher import playfair, affine, hill, simpleVigenere, autoKeyVigenere, fullVigenere, extendedVigenere
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

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

@app.route('/vigenere/simple', methods=["GET", "POST"])
def simple_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            plainteks = request.form["plainteks"]
            key = request.form["key"]
            result = simpleVigenere.simpleVigenereEncrypt(plainteks, key)

            return render_template("simple_vigenere.html", data=result, encrypt=True, fileContent="")
        elif request.form["enc_dec_mode"] == "Decrypt":
            cipherteks = request.form["cipherteks"]
            key = request.form["key"]
            result = simpleVigenere.simpleVigenereDecrypt(cipherteks, key)

            return render_template("simple_vigenere.html", data=result, encrypt=False, fileContent="")
    
    fileContent = ""
    if 'fileContent' in session:
        fileContent = session['fileContent']
    return render_template("simple_vigenere.html", data=simpleVigenere.emptyResult(), fileContent=fileContent)

@app.route('/vigenere/autokey', methods=["GET", "POST"])
def auto_key_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            plainteks = request.form["plainteks"]
            key = request.form["key"]
            result = autoKeyVigenere.autoKeyVigenereEncrypt(plainteks, key)

            return render_template("auto_key_vigenere.html", data=result, encrypt=True, fileContent="")
        elif request.form["enc_dec_mode"] == "Decrypt":
            cipherteks = request.form["cipherteks"]
            key = request.form["key"]
            result = autoKeyVigenere.autoKeyVigenereDecrypt(cipherteks, key)

            return render_template("auto_key_vigenere.html", data=result, encrypt=False, fileContent="")
    
    fileContent = ""
    if 'fileContent' in session:
        fileContent = session['fileContent']
    return render_template("auto_key_vigenere.html", data=autoKeyVigenere.emptyResult(), fileContent=fileContent)

@app.route('/vigenere/full', methods=["GET", "POST"])
def full_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            plainteks = request.form["plainteks"]
            key = request.form["key"]
            result = fullVigenere.fullVigenereEncrypt(plainteks, key)
            session["full_vigenere"] = result
            session["full_vigenere_encrypt"] = True

            return render_template("full_vigenere.html", data=result, encrypt=True, fileContent="")
        elif request.form["enc_dec_mode"] == "Decrypt":
            cipherteks = request.form["cipherteks"]
            key = request.form["key"]
            print(cipherteks, key)
            result = fullVigenere.fullVigenereDecrypt(cipherteks, key)
            session["full_vigenere"] = result
            session["full_vigenere_encrypt"] = False

            return render_template("full_vigenere.html", data=result, encrypt=False, fileContent="")
    
    fileContent = ""
    if 'fileContent' in session:
        fileContent = session['fileContent']
    return render_template("full_vigenere.html", data=fullVigenere.emptyResult(), fileContent=fileContent)

@app.route('/vigenere/full/table', methods=["GET", "POST"])
def full_vigenere_table():
    if request.method == "POST":
        fullVigenere.generateTable()
    table = fullVigenere.showTable()

    if "full_vigenere" in session:
        if session["full_vigenere_encrypt"]:
            return render_template('full_vigenere_table.html', data=session["full_vigenere"], fileContent="", table=table, encrypt=True)
        else:
            return render_template('full_vigenere_table.html', data=session["full_vigenere"], fileContent="", table=table, encrypt=False)
    else:
        return render_template('full_vigenere_table.html', data=fullVigenere.emptyResult(), fileContent="", table=table)

@app.route('/vigenere/extended', methods=["GET", "POST"])
def extended_vigenere_page():
    if request.method == "POST":
        if request.form["enc_dec_mode"] == "Encrypt":
            filename = session["vigenere_extended_filename"]
            key = request.form["key"]
            outputFileName = request.form["outputFileName"]
            result = extendedVigenere.extendedVigenereEncrypt(filename, key, outputFileName)

            return render_template("extended_vigenere.html", data=result, encrypt=True)
        elif request.form["enc_dec_mode"] == "Decrypt":
            filename = session["vigenere_extended_filename"]
            key = request.form["key"]
            outputFileName = request.form["outputFileName"]
            result = extendedVigenere.extendedVigenereDecrypt(filename, key, outputFileName)
            
            return render_template("extended_vigenere.html", data=result, encrypt=False)
    
    filename = ""
    if "vigenere_extended_filename" in session:
        filename = session["vigenere_extended_filename"]
    
    if "vigenere_extended_mode" in session:
        if session["vigenere_extended_mode"] == "radioEncrypt":
            return render_template("extended_vigenere.html", data=extendedVigenere.emptyResult(filename), encrypt=True)
        elif session["vigenere_extended_mode"] == "radioDecrypt":
            return render_template("extended_vigenere.html", data=extendedVigenere.emptyResult(filename), encrypt=False)
    
    return render_template("extended_vigenere.html", data=extendedVigenere.emptyResult(filename), encrypt=True)


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
    return redirect('/')

@app.route('/upload-vigenere/<vtype>', methods = ['GET', 'POST'])
def upload_file_vigenere(vtype):
    if request.method == 'POST':
        if vtype == "extended":
            f = request.files['file']
            filename = f.filename
            f.save(f"./static/dump/{filename}")
            session['vigenere_extended_filename'] = filename
            session['vigenere_extended_mode'] = request.form["enc_dec_mode"]
            return redirect(url_for('extended_vigenere_page'))
        
        f = request.files['file']
        f.save(f"./cipher/dump/{vtype}-input.txt")
        f = open(f"./cipher/dump/{vtype}-input.txt")
        if vtype == "simple":
            fileContent = f.read()
            session['fileContent'] = fileContent
            return redirect(url_for('simple_vigenere_page', fileContent=fileContent))
        if vtype == "auto-key":
            fileContent = f.read()
            session['fileContent'] = fileContent
            return redirect(url_for('auto_key_vigenere_page', fileContent=fileContent))
        if vtype == "full":
            fileContent = f.read()
            session['fileContent'] = fileContent
            return redirect(url_for('full_vigenere_page', fileContent=fileContent))
        # if vtype == "extended":
        #     return redirect(url_for(extended, fileContent=f.read()))
        # return redirect(url_for())
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)