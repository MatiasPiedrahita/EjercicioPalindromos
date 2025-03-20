#Identificador palindromo
#coding = utf-8
import unicodedata
def quitar_tildes(frase):
    return ''.join(c for c in unicodedata.normalize('NFD', frase) if unicodedata.category(c) != 'Mn')

def comprobarPalindormo(frase):
    fraseOriginal = frase
    fraseOriginal = list(fraseOriginal.lower())
    frase = list(frase.lower())
    frase.reverse()
    frase = [letra for letra in frase if letra not in [" ", ",", ".", ";", ":"]]
    fraseOriginal = [letra for letra in fraseOriginal if letra not in [" ", ",", ".", ";", ":"]]
    if fraseOriginal == frase:
        return True
    else:
        return False

frase = input("Ingrese una frase para comprobar si es un palindromo: \n")
fraseSinModificar = frase
frase = quitar_tildes(frase)
esPalindormo = comprobarPalindormo(frase)
if esPalindormo == True:
    print(f"La frase ´{fraseSinModificar}´ se escribe igual de izquierda a derecha y de derecha a izquierda, por lo tanto es un palindromo")
else:
    print(f"La frase ´{fraseSinModificar}´ NO se escribe igual de izquierda a derecha y de derecha a izquierda, por lo tanto NO es un palindromo")
