from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        include_digits = 'digits' in request.form
        include_special = 'special' in request.form

        char_set = string.ascii_letters
        if include_digits:
            char_set += string.digits
        if include_special:
            char_set += string.punctuation

        password = ''.join(random.choice(char_set) for _ in range(length))

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
