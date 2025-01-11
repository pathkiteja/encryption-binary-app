from flask import Flask, render_template, request
import threading
import webbrowser

app = Flask(__name__)

# 🔒 Caesar Cipher Function (Unchanged)
def caesar_cipher(text, key, mode='encode'):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key if mode == 'encode' else -key
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

# 🔢 Binary Conversion Function
def number_to_binary(number):
    try:
        return bin(int(number))[2:]  # Convert to binary without '0b'
    except ValueError:
        return "Invalid input. Please enter a valid number."

# 🏠 Home Route
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    binary_result = ""

    if request.method == "POST":
        if "input_text" in request.form:
            # Caesar Cipher Logic
            text = request.form.get("input_text", "")
            key = int(request.form.get("key", 0))
            mode = request.form.get("mode", "encode")
            result = caesar_cipher(text, key, mode)

        elif "binary_input" in request.form:
            # Binary Converter Logic
            number = request.form.get("binary_input", "")
            binary_result = number_to_binary(number)

    return render_template("index.html", result=result, binary_result=binary_result)

# 🌐 Auto Open Browser
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
