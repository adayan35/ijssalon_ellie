prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}

a = int((prijzen["vanille"]))
b = 0.8
aanbieding = a * b

reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}.")
reclame_tekst3 = reclame_tekst.upper()
reclame_tekst4 = reclame_tekst3

for el in reclame_tekst4:
    if (len((reclame_tekst4[0:7]) >= 5)):
        print((reclame_tekst4[0:7]).upper())
    
    else:
        print((reclame_tekst4[0:7]).lower())