#oef03

#namespace aanmeken via from
from datetime import datetime

limit = datetime.now().year
geboortejaar = int(input("Geef je geboortejaar in: "))

if (limit - geboortejaar >= 18):
    print("Ok, Umag alcohol drinken")
else:
    print("U bent nog geen 18! \n Kom volgend jaar terug.")
