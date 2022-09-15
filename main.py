phrase = "Il y a huit mots dans cette phrase"

def count_words(string):
    nombre = len(string.split())
    return nombre

print("---------------------------------------------------")
print("Phrase écrite : ", phrase)
print("---------------------------------------------------")
print("Nombre de mots :", count_words(phrase))
print("---------------------------------------------------")