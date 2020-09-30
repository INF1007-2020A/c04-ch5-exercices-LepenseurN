#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        return -1*number
    else :
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    MaListe = list()

    for i in range(0,len(prefixes)) :
        MaListe.append(prefixes[i] + suffixe)
    
    return MaListe


def prime_integer_summation() -> int:
    i = 3
    k = 7
    som = 10                     #som est initialisée avec la somme des 03 premiers entiers premiers
    while i < 100 :
        is_prime = True
        for j in range (2 , (k // 2) + 1) :
            if k % j == 0 :
                is_prime = False
        if is_prime :
            i +=1
            som += k
        k += 2
        

    return som


def factorial(number: int) -> int:
    if number == 0 :
        return  1
    else :
        return number * factorial(number-1)


def use_continue() -> None:
    for i in range(1,11) :
        if i == 5 :
            pass
        else :
            print(i)



def verify_ages(groups: List[List[int]]) -> List[bool]:
    list_reponse = list()
    for sous_liste in groups :
        if 25 in sous_liste :
            list_reponse.append(True)
        else :
            if len(sous_liste) > 10 or len(sous_liste) <= 3 :
                list_reponse.append(False)
                continue 
            for elt in sous_liste :
                if elt < 18 :
                    list_reponse.append(False)
                    break
                if 50 in sous_liste and elt > 70 :
                    list_reponse.append(False)
                    break
    return list_reponse


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
