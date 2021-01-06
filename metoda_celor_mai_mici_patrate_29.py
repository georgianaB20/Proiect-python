import numpy as np
import os.path
import sys
import matplotlib.pyplot as plt
import sklearn.datasets 

def creeaza_dreapta(puncte):
    suma_x2=0
    suma_xy=0
    suma_x=0
    suma_y=0
    for punct in puncte:
        suma_x+=punct[0]
        suma_y+=punct[1]
        suma_x2+=punct[0]**2
        suma_xy+=punct[0]*punct[1]
    m=(len(puncte)*suma_xy-(suma_x*suma_y))/(len(puncte)*suma_x2-suma_x**2)
    b=(suma_y-m*suma_x)/len(puncte)
    return m,b

def genereaza_puncte_pe_dreapta(m,b,puncte):
    coord_x=[np.min(puncte[:,0]),np.max(puncte[:,0])]
    coord_y=[]
    for x in coord_x:
        coord_y.append(m*x+b)
    return coord_x,coord_y

def get_x_y(puncte):
    x=[]
    y=[]
    for punct in puncte:
        x.append(punct[0])
        y.append(punct[1])
    return x,y

if __name__=="__main__":
    puncte=[]
    print("Preluati datele din fisier sau doriti generarea lor? fisier/generare")
    tip=input()
    if tip=="fisier":
    #citim datele din fisier
        print("Introduceti numele fisierului de unde doriti sa preluam datele:")
        fisier=input()

        #verificam daca fisierul exista
        if os.path.isfile(fisier) == False:
            print("Fisierul nu exista.")
            quit()

        f=open(fisier,"r")
        puncte=np.array([[float(num) for num in line.split(",")] for line in f])
        f.close()
    elif tip=="generare":
        data = sklearn.datasets.load_wine()
        puncte=data.data[:,:2]
    #print(puncte)
    else:
        print("Optiunea nu exista.")
        quit()

    for punct in puncte:
        print("("+str(punct[0])+","+str(punct[1])+"),")

    #print(len(puncte))
    #calculam dreapta si generam puncte pentru crearea graficului
    m,b=creeaza_dreapta(puncte)
    new_x,new_y=genereaza_puncte_pe_dreapta(m,b,puncte)

    x,y=get_x_y(puncte)
    plt.plot(x,y,'ro')
    plt.plot(new_x,new_y,'g-')
    plt.ylabel("Y")
    plt.xlabel("X")
    x1,x2,y1,y2=plt.axis()
    plt.axis((min(x1,y1)-3,max(x2,y2)+3,min(x1,y1)-3,max(x2,y2)+3))
    titlu="Ecuatia dreptei: "

    m=format(m,".4f")
    if b<0:
        b=format(b,".4f")
        titlu+="{}x{}".format(m,b)
        #print("{}x{}".format(m,b))
        print(titlu)
    else:
        b=format(b,".4f")
        titlu+="{}x+{}".format(m,b)
        #print("{}x+{}".format(m,b))
        print(titlu)

    plt.title(titlu)
    plt.show()





