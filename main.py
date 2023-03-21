from flask import Flask, render_template
import random
import string


def lettersnumbers():
    letters_n_numbers = string.ascii_letters + string.digits + string.punctuation
    rand_string =  ''.join(random.choice(letters_n_numbers) for i in range(random.randint(12, 14)))
    counter = 0
    for i in rand_string:
        if i in string.punctuation:
            counter = counter + 1
    if set(string.digits) & set(rand_string) and set(string.punctuation) & set(rand_string) and counter == 1:
        return rand_string
    else:
        return lettersnumbers()



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html") + lettersnumbers()








app.run()