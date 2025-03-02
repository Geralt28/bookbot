from stats import LiczbaSlow, ReadBook, LiczbaZnakow, Sortuj_tylko_litery
import string, sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status 1 (error)

    # sciezka ksiazki
    sciezka = sys.argv[1]

    # otworz i odczytaj ksiazke
    ksiazka = ReadBook(sciezka)

    liczba_slow = LiczbaSlow(ksiazka)
    liczba_znakow = LiczbaZnakow(ksiazka)
    lista_sort = Sortuj_tylko_litery(liczba_znakow)
    
    # kod do wydruku, mozna by ubrac w osobna fukcje
    print(f"--- Begin report of {sciezka} ---")
    print(f"{liczba_slow} words found in the document")
    print("")
    for pozycja in lista_sort:
        print(f"{pozycja["litera"]}: {pozycja["liczba"]}")
    print("--- End report ---")


main()