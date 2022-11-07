import random 
from codeanote import *
lereminu = ["a","z","e","r","t","y",'u',"i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"," ","?",".","!","#","@","(",")","=","+","-"]
leremag = ["A","Z","E","R","T","Y",'U',"I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]


def random_mag():
    x = random.choice(leremag)
    ' '.join(str(e) for e in x)
    return(x)

def random_minu():
    x = random.choice(lereminu)
    if x == " ":
        x = random_mag()
    return(x)


nnlist=[]
pnnluist=[]


résulta = ""

def génareur():
    nn = 0
    for i in lereminu :
        randome = random_minu()
        if randome in pnnluist : 
            randome = random_mag()
        résulta = (str(i) + " = " + randome + " = " + str(nn))
        print(résulta)
        nnlist.append(str(i))
        pnnluist.append(randome)
        nn = nn + 1 
    print(nnlist,pnnluist)
    with open("codeanote.py", "r+") as f:
        old = f.read()
        f.seek(0)
        f.write("bon = "+str(nnlist)+"\n" + old)
        f.write("pasbon = "+str(pnnluist)+"\n" + old)

def encodin(mères) :
    code = ""
    for i in mères:
        pov = bon.index(i)
        code = code + pasbon[pov]
    return code

def déencodin(mères) :
    code = ""
    for i in mères:
        pov = pasbon.index(i)
        code = code + bon[pov]
    return code