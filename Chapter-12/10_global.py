a = 89

def fun():
    global a #Global is a key word which will keep the value of a in the func throught out the program
    a = 3
    print(a)

fun()
print(a)