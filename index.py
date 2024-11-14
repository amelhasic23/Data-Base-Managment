import sqlite3

# Kreiranje baze podataka i tabele
conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              year INTEGER)''')

# Funkcija za unos knjige
def add_book():
    title = input("Unesite naziv knjige: ")
    year = int(input("Unesite godinu izdanja: "))
    c.execute("INSERT INTO Books (title, year) VALUES (?, ?)", (title, year))
    conn.commit()
    print("Knjiga uspešno dodata u bazu.")

# Funkcija za ispis svih knjiga
def display_books():
    c.execute("SELECT * FROM Books")
    books = c.fetchall()
    if books:
        print("Sve knjige u bazi:")
        for book in books:
            print(f"ID: {book[0]}, Naziv: {book[1]}, Godina izdanja: {book[2]}")
    else:
        print("Nema knjiga u bazi.")

# Glavna petlja za unos i ispis knjiga
while True:
    print("\nIzaberite opciju:")
    print("1. Dodaj knjigu")
    print("2. Ispis svih knjiga")
    print("3. Izlaz")

    choice = input(">> ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        break
    else:
        print("Nepostojeća opcija. Molimo unesite ponovo.")
    
# Zatvaranje konekcije
conn.close()
