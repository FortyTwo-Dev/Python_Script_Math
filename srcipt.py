# ce programme a besoin de 2 modules time et math #
import time
import math
# fonction qui sert à demander des valeurs pour les points A(coordonnée X et Y) et B(coordonnée X et Y) #
def XY():
    global Xa, Xb, Ya, Yb , A, B
    Xa = float(input("Rentrer la valeur Xa : "))

    Ya = float(input("Rentrer la valeur Ya : "))

    A = [Xa, Ya]

    print(A)
    Xb = float(input("Rentrer La Valeur Xb : "))

    Yb = float(input("Rentrer La Valeur Yb : "))

    B = [Xb, Yb]

    print(B)
    print("A", A , ", " , "B",B)



# fonction qui sert à demander ce que l'on va faire des nombres (trouver le milieu de A et B, calculer la distance entre A et B) #
# il suffit d'écrire la lettre entre "- -" qui est demandé et Si il n'est pas demander une lettre spécifique il faut mettre un O = (oui) #
def calcul():
    if input("Valider-O- Recommencer-N- : ") == "O":
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
            # arr = arrondi
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

            
            
def Vecteur():
    if input("Validé-O- Recommencer-N- : ") == "O":
        resultVX = (Xb - Xa)
        resultVY = (Yb - Ya)
        print("(",resultVX,")")
        print("(",resultVY,")")
        
        
        
# fonction Menu qui sert à demander ce que l'on veux faire ( calcul de milieu, distance ou garder les mêmes valeurs) #
def Menu():
    H = True
    S = 2
    while  H == True:
        if input("Milieu ~ Distance XY : ") == "XY": 
            XY()
            calcul()
        elif input("Vecteur : ") == "V":
            XY()
            Vecteur()
        else:
            print("Fin Des Choix Attendre " , S, "Sec")
            time.sleep(S)


Menu()


# V1.5 #
# Attention Si il y a une erreur effacer le texte entre "# #" #
