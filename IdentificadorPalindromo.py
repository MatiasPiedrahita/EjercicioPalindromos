#Identificador palindromo
#coding = utf-8
def comprobarPalindormo(frase):
    fraseOriginal = frase
    fraseOriginal = list(fraseOriginal.lower())
    frase = list(frase.lower())
    frase.reverse()
    frase = [elemento for elemento in frase if elemento not in [" "]]
    fraseOriginal = [elemento for elemento in fraseOriginal if elemento not in [" "]]
    if fraseOriginal == frase:
        return True
    else:
        return False

frase = input("Ingrese una frase para comprobar si es un palindromo: \n")
esPalindormo = comprobarPalindormo(frase)
if esPalindormo == True:
    print(f"La frase {frase} se escribe igual de izquierda a derecha y de derecha a izquierda, por lo tanto es un palindromo")
else:
    print(f"La frase {frase} NO se escribe igual de izquierda a derecha y de derecha a izquierda, por lo tanto NO es un palindromo")