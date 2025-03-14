

def ReadBook(sciezka):
    with open(sciezka) as f:
        return f.read()

def LiczbaSlow(tekst: str):
    slowa = tekst.split()
    return (len(slowa))

def LiczbaZnakow(tekst):
    tekst_low = tekst.lower()
    liczenie_znakow = {}  # Pusty slownik do liczenia wystapien
    
    #to bylo sprytne ale musze uwzgledniac tez symbole 
    #wiec zastapilem na dynamiczne dodawanie w petli
    #liczenie_liter = {char: 0 for char in string.ascii_lowercase}
    #liczenie_liter[" "] = 0  # dodac spacje
    
    for znak in tekst_low:
        if znak not in liczenie_znakow:
            liczenie_znakow[znak] = 1
        else:
            liczenie_znakow[znak] += 1
    return liczenie_znakow

def Sortuj_tylko_litery(liczba_znakow):
    # funkcja zamienie slownik w liste slownikow (?), wybiera jedynie litery z alfabetu, sortuje
    #lista_znakow = [{"char": k, "count": v} for k, v in liczenie_liter.items()]
    lista = []

    #for i in range(len(liczba_znakow)):
    for litera in liczba_znakow:
        if litera.isalpha():
            lista.append({"litera": litera, "liczba": liczba_znakow[litera]})
    
    lista.sort(key=lambda x: x["liczba"], reverse=True)  
    
    return lista