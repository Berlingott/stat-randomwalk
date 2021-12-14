# Python code for 2D random walk.

import numpy
import pylab
import random
import math

def generalN():
    nombredepas = 10 #nombre de pas
    nombredepas = nombredepas + 1
    return nombredepas
x = numpy.zeros(generalN())
y = numpy.zeros(generalN())
moyenneaucarreMarcheSimpleX = numpy.zeros(generalN())
moyenneaucarreMarcheSimpleY = numpy.zeros(generalN())

moyenneaucarreMarcheSansReculX = numpy.zeros(generalN())
moyenneaucarreMarcheSansReculY = numpy.zeros(generalN())

moyenneaucarreMarchePassageUniqueX = numpy.zeros(generalN())
moyenneaucarreMarchePassageUniqueY = numpy.zeros(generalN())


def marcheAleatoiresimple(nombreiterationselonN):
    i = 0
    #nombreiterationselonN = generalN()
    while i < nombreiterationselonN:
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            i = i + 1
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            i = i + 1
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            i = i + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            i = i + 1

def marcheAleatoireSansRecul(nombredepas):
    i = 1
    while i < nombredepas:
        val = random.randint(1, 4)
        if val == 1:
            if x[i - 1] + 1 != x[i - 2]:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
                i = i + 1
        elif val == 2:
            if x[i - 1] - 1 != x[i - 2]:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
                i = i + 1
        elif val == 3:
            if y[i - 1] + 1 != y[i - 2]:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
                i = i + 1
        else:
            if y[i - 1] - 1 != y[i - 2]:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1
                i = i + 1

def sommesNousDejaPassezParLa(positionX,positionY,i):
    iterationdetest = 0
    while iterationdetest < i:
        if positionX == x[iterationdetest] and positionY == y[iterationdetest]:
            return False
        iterationdetest = iterationdetest + 1
    return True

def CheckSiBloquer(i):
        if sommesNousDejaPassezParLa(x[i - 1] + 1, y[i - 1], i):
            return False
        if sommesNousDejaPassezParLa(x[i - 1] - 1, y[i - 1], i):
            return False
        if sommesNousDejaPassezParLa(x[i - 1], y[i - 1] + 1, i):
            return False
        if sommesNousDejaPassezParLa(x[i - 1], y[i - 1] - 1, i):
            return False
        return True


def marcheAPassageUnique(nombredepas):
    i = 1
    while i < nombredepas:
        val = random.randint(1, 6)
        if val == 1:
            if sommesNousDejaPassezParLa(x[i - 1] + 1, y[i - 1], i):
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
                i = i + 1
        elif val == 2:
            if sommesNousDejaPassezParLa(x[i - 1] - 1, y[i - 1], i):
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
                i = i + 1
        elif val == 3:
            if sommesNousDejaPassezParLa(x[i - 1] , y[i - 1] + 1, i):
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
                i = i + 1
        elif val == 4:
            if sommesNousDejaPassezParLa(x[i - 1], y[i - 1] - 1, i):
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1
                i = i + 1
            else:
                if CheckSiBloquer(i):
                    i = 0
    # Generation de carte



def GenerationDeGraph(titre):
    pylab.title(titre + " ($n = " + str(generalN() - 1) + "$ steps)")
    pylab.plot(x, y)

    pylab.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
    pylab.show()

def lancementDeFonction(fonctionChoisit, typeDeMarcheSuivi):
    if fonctionChoisit == 1 and typeDeMarcheSuivi == 1:
        marcheAleatoiresimple(generalN())
        GenerationDeGraph("Marche aléatoire simple ")
    elif fonctionChoisit == 1 and typeDeMarcheSuivi == 2:
        marcheAleatoireSansRecul(generalN())
        GenerationDeGraph("Marche aléatoire sans recul")
    elif fonctionChoisit == 1 and typeDeMarcheSuivi == 3:
        marcheAPassageUnique(generalN())
        GenerationDeGraph("Marche aléatoire à passage unique ")
    elif fonctionChoisit == 2:
        moyenneMarcheCourbe()

def moyenneMarcheCourbe():
    n = generalN()
    i = 0
    donnedansx = 0
    donnedansy = 0
    nombredetest = 10000
    j = 0
    k = 0
    totaldestest = 0
    test = numpy.zeros(nombredetest)
    while i < n:
        while j < nombredetest:
            marcheAleatoiresimple(i)
            donnedansx = x[i-1]
            donnedansy = y[i-1]
            donnedansx = donnedansx*donnedansx
            donnedansy = donnedansy*donnedansy
            test[j] = donnedansx+donnedansy
            j = j + 1
        while k < nombredetest:
            totaldestest = totaldestest + test[k]
            k = k + 1
        moyenneaucarreMarcheSimpleX[i] = i
        print(str(totaldestest/nombredetest))
        moyenneaucarreMarcheSimpleY[i] = totaldestest/nombredetest
        print(str(moyenneaucarreMarcheSimpleX[i]) + "," + str(moyenneaucarreMarcheSimpleY[i]))
        i = i+1
        j = 0
        k = 0
        totaldestest = 0
    pylab.title("Distance parcouru au carré (n = " + str(generalN() - 1) + "$ pas," + str(nombredetest) + "essaies par nombre de pas)")
    pylab.plot(moyenneaucarreMarcheSimpleX, moyenneaucarreMarcheSimpleY)

    i = 0
    totaldestest = 0
    while i < n:
        while j < nombredetest:
            marcheAleatoireSansRecul(i)
            donnedansx = x[i - 1]
            donnedansy = y[i - 1]
            donnedansx = donnedansx * donnedansx
            donnedansy = donnedansy * donnedansy
            test[j] = donnedansx + donnedansy
            j = j + 1
        while k < nombredetest:
            totaldestest = totaldestest + test[k]
            k = k + 1
        moyenneaucarreMarcheSansReculX[i] = i
        print(str(totaldestest / nombredetest))
        moyenneaucarreMarcheSansReculY[i] = totaldestest / nombredetest
        print(str(moyenneaucarreMarcheSansReculX[i]) + "," + str(moyenneaucarreMarcheSansReculY[i]))
        i = i + 1
        j = 0
        k = 0
        totaldestest = 0

    pylab.plot(moyenneaucarreMarcheSansReculX, moyenneaucarreMarcheSansReculY)

    i = 0
    totaldestest = 0
    while i < n:
        while j < nombredetest:
            marcheAPassageUnique(i)
            donnedansx = x[i - 1]
            donnedansy = y[i - 1]
            donnedansx = donnedansx * donnedansx
            donnedansy = donnedansy * donnedansy
            test[j] = donnedansx + donnedansy
            j = j + 1
        while k < nombredetest:
            totaldestest = totaldestest + test[k]
            k = k + 1
        moyenneaucarreMarchePassageUniqueX[i] = i
        print(str(totaldestest / nombredetest))
        moyenneaucarreMarchePassageUniqueY[i] = totaldestest / nombredetest
        print(str(moyenneaucarreMarcheSansReculX[i]) + "," + str(moyenneaucarreMarcheSansReculY[i]))
        i = i + 1
        j = 0
        k = 0
        totaldestest = 0

    pylab.plot(moyenneaucarreMarchePassageUniqueX, moyenneaucarreMarchePassageUniqueY)

    pylab.savefig("Moyenne marche aléatoire" + str(n) + ".png", bbox_inches="tight", dpi=1800)
    pylab.show()

if __name__ == '__main__':
    # choix de l'utilisateur
    typeDeMarcheSuivi = 1
    n = 10000
    print("1) Génération d'une carte de marche aléatoire")
    print("2) Génération d'un graphique de la distance au carré")
    fonctionChoisit = int(input("Choix de la fonction:"))
    if fonctionChoisit == 1:
        print("1) Marche aléatoire")
        print("2) Marche aléatoire sans reculer")
        print("3) Marche à passage unique")
        typeDeMarcheSuivi = int(input("Choix de la marche:"))
    lancementDeFonction(fonctionChoisit, typeDeMarcheSuivi)