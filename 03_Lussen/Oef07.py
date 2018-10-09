#oef 07

startwaarde = int(input("Geef de startwaarde in: "))
positievestapgrootte = int(input("Geef een positievestapgrootte in: "))
teprintenGetal = int(input("Geef een aantal getallen in dat uitgeprint moet worden: "))

for index in range(startwaarde,(teprintenGetal*positievestapgrootte)+1 ,positievestapgrootte):
    print(index)
