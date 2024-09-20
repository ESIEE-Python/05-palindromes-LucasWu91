"""
Fichier main.py
"""
#### Fonction secondaire

def ispalindrome(p):
    """
        Vérifie si le mot est un palyndrome
        Args :
            p chaîne de caractere

        Returns : 
            True or False
    """
    table = str.maketrans(
        "àáâäãçéèêëíìîïñóòôöõùúûüýÿÀÁÂÄÃÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÙÚÛÜÝŸ",
        "aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUYY",
        " .,;:!?'()-" )
    p=p.translate(table).lower()
    a=p[::-1]
    if a == p :
        return True
    return False
#### Fonction principale


def main():
    """
    Test différentes valeurs
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
