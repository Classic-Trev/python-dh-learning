def greet_latin(name):
    return f"Salve, {name}!"
def farewell_latin(name):
    return f"Vale, {name}!"
print(greet_latin("Marcus"))
print(greet_latin("Julia"))
print(farewell_latin("Cicero"))
#not case correct! Let's fix it!

def greet_latin(name):
    if name.endswith("us"):
        name = name[:-2] + "e"
    return f"Salve, {name}!"
def farewell_latin(name):
    if name.endswith("us"):
        name = name[:-2] + "e"
    return f"Vale, {name}!"
print(greet_latin("Marcus"))
print(greet_latin("Julia"))
print(farewell_latin("Cicero"))
#HELL YEAH LETS GOOOOOOO