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

    
def ABC():
    global a, b, c
    a = float(input("rentrer la valeur A : "))
    b = float(input("rentrer la valeur B : "))
    c = float(input("rentrer la valeur C : "))
    print(f"\nA : {a},\nB : {b},\nC : {c}")
# fonction qui sert à demander ce que l'on va faire des nombres (trouver le milieu de A et B, calculer la distance entre A et B) #
# il suffit d'écrire la lettre entre "- -" qui est demandé et Si il n'est pas demander une lettre spécifique il faut mettre un O = (oui) #
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


# New #
def FonctionAffine():
    print("Sert a trouvé m")
    if input("Validé-O- Recommencer-N- : ") == "O":
        M_Affine = (Yb - Ya)/(Xb - Xa)
        print(M_Affine)


            
def Vecteur():
    if input("Validé-O- Recommencer-N- : ") == "O":
        resultVX = (Xb - Xa)
        resultVY = (Yb - Ya)
        print("(", resultVX, ")")
        print("(", resultVY, ")")
        if input("Vecteur multiplier ? : ") == "O":
            AU = float(input("rentrez une valeur : "))
        else:
            AU = 1
        print("(", AU * resultVX, ")")
        print("(", AU * resultVY, ")")

        
        
def Colinearite():
    if input("Validé-O- Recommencer-N- : ") == "O":
        Coli1 = (Xa * Yb)
        Coli2 = (Xb * Ya)
        Coli = ((Xa * Yb) - (Xb * Ya))
        print(Coli1)
        print(Coli2)
        print(Coli)
        if Coli == 0:
            print("c'est colineaire :) ", Coli)
        else:
            print("ce n'est pas colineaire", Coli)



def VDT():
    vdt = True
    Vdt = input("que cherchez-vous : ")
    while vdt == True:
        if Vdt == "V":
            D = float(input("enter D : "))
            T = float(input("enter T : "))
            CV = D/T
            print("V = ", CV)
            vdt = False
        elif Vdt == "D":
            V = float(input("enter V : "))
            T = float(input("enter T : "))
            CV = V*T
            print("D = ", CV)
            vdt = False
        else:
            V = float(input("enter V : "))
            D = float(input("enter D : "))
            CV = D/V
            print("T = ", CV)
            vdt = False
    if input("Convertir-C- quitter-Q- : ") == "C":
        print("convertir")
        print("m/s -> k/h = M")
        print("k/h -> m/s = K")
        if input("M ? K ? : ") == "M":
            CV = CV * 3.6
            print(CV," K/h")
        else:
            CV = CV/3.6
            print(CV, "M/s")  
        
        
def Canonique():
    alpha = -b/(2*a)
    beta = -((b**2)-4*a*c)/4*a
    print("alpha = ", alpha)
    print("beta = ", beta)    
    
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
        elif input("Colinearite : ") == "C":
            XY()
            Colinearite()
        elif input("Vitesse V=D/T : ") == "V":
            VDT()
        elif input("F(affine) : ") == "F":
            XY()
            FonctionAffine()
        else:
            print("Fin Des Choix Attendre " , S, "Sec")
            time.sleep(S)


Menu()


# V3.0 #
# Milieu #
# Distance #
# Colinearite #
# Vitesse V=D/T #
# Vecteur #
# F(Affine) : pour trouver "m" #
# Attention Si il y a une erreur effacer le texte entre "# #" #
