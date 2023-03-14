from flask import Flask
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


html = ''' 
<html> 
 <head> 
 <style> 
 html { 
 color: white; 
 background-image: url("https://is5-ssl.mzstatic.com/image/thumb/Music122/v4/e2/1d/81/e21d812e-3290-11bb-dced-4b3963b731dd/196922264559_Cover.jpg/1200x1200bf-60.jpg"); 
 } 
 p{ 
 font-size: 4em; 
 } 
 </style> 
 </head> 
 <body> 
 <form action = "/" method = post" 
 <p>Сгенерируйте свой пароль:</p> 
 <p><f'{lettersnumbers()}/ 
 <p><input type = "submit" value = "Сгенерировать"/></p> 
 </form> 
 </body> 
</html> 
'''
app = Flask(__name__)


@app.route("/")
def index():
    return f'{html}' \
           f'{lettersnumbers()}'

app.run()