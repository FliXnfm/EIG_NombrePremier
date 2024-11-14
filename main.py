"""
Module pour vérifier les nombres premiers et les lister jusqu'à une limite donnée.
"""

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """Vérifie si un nombre est premier.

    Args:
        p (int): Le nombre à vérifier.

    Returns:
        bool: True si p est un nombre premier, False sinon.
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True

#### Fonction principale

def main():
    """Fonction principale pour lister les nombres premiers jusqu'à 100."""
    # Appels à la fonction secondaire
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
