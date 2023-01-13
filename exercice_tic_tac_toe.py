#mohamed amin jelloul
from numpy import array
from random import randint


# la saisie de N (c'est une matrice carre avec N impaire )
def saisir():
    valid=False
    while valid==False:
        N=randint(3,10)
        if N%2!=0:
            valid=True
    return N


#remplir la matrice avec des etoiles
def remplir_mat(M,N):
    for i in range(N):
        for j in range(N):
            M[i,j]="*"

#fonction pour verifier qui est le gagnant
def verif(M,N,nbr):
    ch1=""
    ch2=""
    XN=N-1
    #premier boucle pour verifier les diagonales de la matrice
    for i in range(N):
        ch1=M[i,i]+ch1
        ch2=M[XN,i]+ch2
        XN=XN-1
    V1=True
    V2=True
    i=0
    j=0
    while(i<=N-1 and V1==True):
        if ch1[i]==ch1[i-1]:
            i=i+1
        else:
            V1=False

    while(j<=N-1 and V2==True):
        if ch2[j]==ch2[j-1]:
            j=j+1
        else:
            V2=False
    if V1==True:
        if ch1[0]=="O":
            #print("cas1") j'ai utilise cet affichage pour chercher les ligne
            #print(ch1)
            return 1
        elif ch1[0]=="X":
            #print("cas2")
            #print(ch1)
            return 2
    elif V2==True:
        if ch2[0]=="O":
            #print("cas3")
            #print(ch2)

            return 1
        elif ch1[0]=="X":
            #print("cas4")
            #print(ch2)
            return 2
    #2eme boucle pour verifier les lignes
    i=0
    V3=False
    while(V3==False and i<=N-1):
        j=0
        ch1=M[i,j]
        j=j+1
        while( (j<=N-1)and(ch1[0]==M[i,j])):
            ch1=ch1+M[i,j]
            j=j+1
        if len(ch1)==N:
            V3=True
        i=i+1
    if V3==True:
        if ch1[0]=="O":
            #print("cas5")
            #print(ch1)
            return 1
        elif ch1[0]=="X":
            #print("cas6")
            #print(ch1)
            return 2

    #3eme boucle pour verifier les colonnes
    j=0
    V4=False
    while(V4==False and j<=N-1):
        i=0
        ch1=M[i,j]
        i=i+1
        while((i<=N-1) and (ch1[0]==M[i,j] ) ):
            ch1=ch1+M[i,j]
            i=i+1
        if len(ch1)==N:
            V4=True
        j=j+1

    if V4==True:
        if ch1[0]=="O":
            #print("cas7")
            #print(ch1)
            return 1
        elif ch1[0]=="X":
            #print("cas8")
            #print(ch1)
            return 2
    if nbr==N*N:
        #print("cas9")
        return 3
    else:
        return 4

def Jouer(M,N):
    #Joueur 1
    nbr=0
    valid=False
    while valid==False:
        S1=input("Joueur 1: saisir votre symbole")
        if S1=="O" or S1=="X":
            valid=True
    #Joueur2
    valid=False
    while valid==False:
        S2=input("Joueur 2: saisir votre symbole")
        if ((S2=="O" or S2=="X") and (S2!=S1)):
            valid=True
    #Joueur 1
    gagnant=4
    while((nbr<N*N) and (gagnant>3)):
        if ((nbr<N*N) and (gagnant>3)):
            print(M)
            valid=False
            while valid==False:
                ii=int(input("J1:saisir la ligne"))
                jj=int(input("J1:saisir la colonne"))
                i=ii-1
                j=jj-1
                if (0<=i<=N-1 and 0<=j<=N-1 and M[i,j]=="*"):
                    valid=True
                    M[i,j]=S1
                    nbr=nbr+1
                    if nbr>=(N*2)-1:
                        gagnant=verif(M,N,nbr)
                else:
                    print("saisir correctement")

    #Joueur 2
        if ((nbr<N*N) and (gagnant>3)):
            print(M)
            valid=False
            while valid==False:
                ii=int(input("J2:saisir la ligne"))
                jj=int(input("J2:saisir la colonne"))
                i=ii-1
                j=jj-1
                if 0<=i<=N-1 and 0<=j<=N-1 and M[i,j]=="*":
                    valid=True
                    M[i,j]=S2
                    nbr=nbr+1
                    if nbr>=(N*2)-1:
                        gagnant=verif(M,N,nbr)
                else:
                    print("saisir correctement")
    #gagnant
    if gagnant==1:
        print("le gagnant qui a le caractere O")
    elif gagnant==2:
        print("le gagnant qui a le caractere X")
    elif gagnant==3:
        print("Partie Null")


N=saisir()
#vous pouvez tester avec N=3 le plus petit entier impair (commenter la ligne precedente et changer N par 3 dans les lignes suivantes
M=array([[int]*N]*N)
remplir_mat(M,N)
Jouer(M,N)
