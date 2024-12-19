import pyperclip  # Modul für den Zugriff auf die Zwischenablage

# Mapping lateinischer Buchstaben zu kyrillischen Lookalikes
latin_to_cyrillic_lookalikes = {
    'A': 'А',
    'a': 'а',
    'E': 'Е',
    'e': 'е',
    'O': 'О',
    'o': 'о',
    'P': 'Р',
    'p': 'р',
    'C': 'С',
    'c': 'с',
    'T': 'Т',
    't': 'т',
    'Y': 'У',
    'y': 'у',
    'X': 'Х',
    'x': 'х',
}


def replace_with_cyrillic_lookalikes(text):
    # Ersetze lateinische Buchstaben durch kyrillische Lookalikes
    return ''.join(latin_to_cyrillic_lookalikes.get(char, char) for char in text)


# Eingabe
input_text = input("Gib den Text ein, der konvertiert werden soll: ")

# Konvertierung
output_text = replace_with_cyrillic_lookalikes(input_text)

# Ausgabe in die Zwischenablage kopieren
pyperclip.copy(output_text)

# Bestätigung
print("Der konvertierte Text wurde in die Zwischenablage kopiert!")
print("Konvertierter Text:", output_text)
