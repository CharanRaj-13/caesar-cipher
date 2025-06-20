from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        key = request.form.get('key', '')
        mode = request.form['mode']

        if mode == 'brute':
            result = ""
            for k in range(1, 26):
                result += f"Key {k}: {caesar_decrypt(text, k)}<br>"
        else:
            try:
                key = int(key)
                if not (1 <= key <= 25):
                    result = "Key must be between 1 and 25"
                else:
                    if mode == 'encrypt':
                        result = caesar_encrypt(text, key)
                    elif mode == 'decrypt':
                        result = caesar_decrypt(text, key)
            except ValueError:
                result = "Invalid key"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
