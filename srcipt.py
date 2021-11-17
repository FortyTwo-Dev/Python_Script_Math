import time
import math

def XY():
    global Xa, Xb, Ya, Yb , A, B
    Xa = float(input("rentrer la valeur Xa : "))

    Ya = float(input("rentrer la valeur Ya : "))

    A = [Xa, Ya]

    print(A)
    Xb = float(input("Rentrer La Valeur Xb : "))

    Yb = float(input("Rentrer La Valeur Yb : "))

    B = [Xb, Yb]

    print(B)
    print("A", A , ", " , "B",B)



    
def calcul():
    if input("Validé-O- Recommencer-N- : ") == "O":
        if input("Milieu-M- : ") == "M":
            resultX = (Xa + Xb)/2
            print("X", resultX)
            resultY = (Ya + Yb)/2
            print("Y", resultY)
            RXY = [resultX, resultY]
            print("K", RXY)
        elif input("Distance-D- : ") == "D":
            resultDX = (Xb - Xa)**2
            resultDY = (Yb - Ya)**2
            resultXYd = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
            result_D = resultDX + resultDY
            print("Racine Carré De ", result_D)
            print("Distance Arr = ", resultXYd)
        elif input("All M And D -MD- : ") == "MD":
            print("Milieu")
            resultX = (Xa + Xb)/2
            print("X", resultX)
            resultY = (Ya + Yb)/2
            print("Y", resultY)
            RXY = [resultX, resultY]
            print("K", RXY)
            print("")
            print("Distance")
            resultDX = (Xb - Xa)**2
            resultDY = (Yb - Ya)**2
            resultXYd = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)
            result_D = resultDX + resultDY
            print("Racine Carré De ", result_D)
            print("Distance Arr = ", resultXYd)

        else:
            XY()
            calcul()



def Menu():
    i = False
    H = True
    S = 2
    while  H == True:
        if input("Milieu ~ Distance XY : ") == "XY": 
            XY()
            calcul()
            i = True
        elif i == True:
            if input("garder les valeurs : ") == "O":
                calcul()
        else:
            print("Fin Des Choix Attendre " , S, "Sec")
            time.sleep(S)


Menu()


# V1.1 #
