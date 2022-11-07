from CHOUSE import *
test = ""
testdé = ""
def pytest() :
    test = encodin("test bonjour")
    testdé = déencodin(test)
    if testdé == "bonjour":
        print("bon")
    else :
        print("pas bon")
        exit