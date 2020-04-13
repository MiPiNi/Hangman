import wordlist


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


win: bool = False
used_chars = []

print("Zaczynam wisielca...")
# Dopuszczlna ilosc bledow
while True:
    incorrect_ans = int(input("Podaj  dozwolona ilosc niepoprawnych odpowiedzi[1-99]: "))
    if 1 <= incorrect_ans <= 99:
        break
    else:
        print("Liczba " + str(incorrect_ans) + " jest poza zakresem!")
        print("Sprobuj ponownie!")
# Minimalna dlugosc slowa
while True:
    min_word = int(input("Podaj minimalna długość słowa: "))
    print("\n")
    print("Wybieram słowo...\n")
    word_check = wordlist.random_word(min_word)
    if word_check == -1:
        print("Nie ma słowa zawierajacego " + str(min_word) + " liter w slowniku!")
        print("Sprobuj ponownie!")
    elif word_check == -2:
        print("Słowo nie może mieć ujemnej lub zerowej ilosci znakow!")
        print("Podana liczba znakow: " + str(min_word))
        print("Sprobuj ponownie!")
    else:
        break #
word = list(wordlist.random_word(min_word))
# print("".join(word)) #DEBUG

word_masked = list(len(word) * "_")

# Usuwanie 'end line'
if list(word)[len(word) - 1] == '\n':
    word_masked.pop(len(word) - 1)
    word.pop(len(word) - 1)

print("".join(word_masked))
word = "".join(word)

# Zgadywanie slowa
while not win:
    char = str(input("Podaj literke: "))
    print("\n")
    if len(char) == 1 and char.isalpha():
        if char in word:
            chars = list(find_all(word, char))
            for i in chars:
                word_masked[i] = char
            print("Literka " + "'" + char + "'" + " znajduję się w wylosowanym słowie!")
            print("Pozostałe niepoprawne odpowiedzi: " + str(incorrect_ans) + "\n")
        else:
            used_chars.append(char)
            print("Literka " + "'" + char + "'" + " nie znajduję się w wylosowanym słowie!")
            incorrect_ans -= 1
            print("Pozostałe niepoprawne odpowiedzi: " + str(incorrect_ans) + "\n")
        guess: str = "".join(word_masked)
        print("Słowo: " + guess)
        if guess == word:
            win = True
        elif incorrect_ans == 0:
            win = False
            break

    else:
        print("Blad!")
        print("Sprawdz czy wpisales LITERE!")
    print("Uzyte litery:" + ", ".join(used_chars) + "\n")

# Sprawdzanie czy wygrales(zgadles) czy przegrales(wykorzytsales dozowlna ilosc bledow)
if win:
    print("Grtulacje!")
    print("Słowo to " + word)
else:
    print("Niestety, przekroczyles dopuszczalna ilosc bledow")
    print("Słowo to " + word)
