from flask import Flask

""" 

Web server – Flask

* Flask är ett lättviktigt Python-ramverk för webbutveckling.
* Används för att skapa webbsidor och API:er.
* Bygger på routing (`@app.route("/")`).
* Har en inbyggd utvecklingsserver.

Exempel:
Gå till mappen där filen ligger och kör kommandot i terminalen:  flask --app learn_lecture run 

eller tryck på "play-knappen" för att starta fil 
"""

#app = Flask(__name__)
#
#@app.route("/")
#def home():
#    return "Hello World"
#
#if __name__ == "__main__":
#    app.run()




"""
Command Line (terminalen)
* mkdir = skapa mapp
* ni = skapa fil (ex ni app.py)
* rm = radera fil (ex rm app.py) 
* cd = byta mapp

"""



"""     
 `__name__` och `__main__ : Special Attributes built into Python`
 
 Vad är __name__?

__name__ är en inbyggd variabel i Python som varje fil (modul) får automatiskt.
Den berättar hur filen används:

Om filen körs direkt: `__name__ == "__main__"`
Om filen importeras i en annan fil, __name__ är filens namn utan .py, e.g:  `__name__` = filens namn



Exempel:
"""

#if __name__ == "__main__":
#    app.run()



"""



Python Functions as First Class Objects

Funktioner är "first class objects" i Python.
Det betyder att de kan:

* Sparas i variabler
* Skickas som argument
* Returneras från andra funktioner
* Vara inuti andra funktioner (nesting)

Exempel:

"""
#def subtract(n1,n2):
#    return n1 - n2
#
#def multiply(n1,n2):
#    return n1 * n2
#
#
#def calculate(calc_function, n1,n2):
#   return calc_function(n1, n2)
#
#sum = calculate(multiply, 10, 5)
#print(sum)
#
#
#
## Nesting:
#def outer():
#    print("i'm outer")
#    def inner():
#        print("I'm inner")
#    inner()
#
#outer()
#
#
## En funktion som returnerar en annan funktion
#
#def outer():
#    print("i'm outer")
#    def inner():
#        print("I'm inner")
#    return inner
#
#inner = outer()               # Kör outer(), får tillbaka funktionen inner
#inner()                       # Kör funktionen inner






"""
Python Decorators & `@` syntax

* En decorator är en funktion som "wrappar" en annan funktion.
* Används för att lägga till extra funktionalitet utan att ändra originalkoden.

"""

##Exempel utan `@`:
#import time
#
## Lägger till extra funktionalitet runt en annan funktion, i detta fall time.sleep
#def decorator_function(function):
#    def wrapper_function():
#        print("Före sov 2 sec")
#        time.sleep(2)
#        function()
#        print("Efter")
#    return wrapper_function
#
#
## Sedan använd decorator för att återanvända gemensam funktionalitet i funktioner
## Dekorerade funktioner med @-syntax
#@decorator_function
#def say_hello():
#    #time.sleep(1)
#    print("Hello")
#
#@decorator_function
#def say_bye():
#    #time.sleep(1)
#    print("Bye")
#
#
## Kör de dekorerade funktionerna
#say_hello()
#say_bye()






"""
Routing 
"""
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/bye')
def bye():
    return 'Bye'


if __name__ == "__main__":
    app.run()











