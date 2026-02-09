def chiffrement_cesare(message, decalage):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_chiffre = ''
    for i in message:
        if i in alphabet:
            lettre = ord(i) + decalage
            if lettre > ord('Z'):
                lettre -= 26
            elif lettre < ord('A'):
                lettre += 26
            message_chiffre += chr(lettre)
        else:
            message_chiffre += i
    return message_chiffre
 
assert chiffrement_cesare("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1) == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
assert chiffrement_cesare("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -1) == "ZABCDEFGHIJKLMNOPQRSTUVWXY"
assert chiffrement_cesare("MANGER DES POMMES", 1) == "NBOHFS EFT QPNNFT"
assert chiffrement_cesare("MANGER DES POMMES", 26) == "MANGER DES POMMES"
assert chiffrement_cesare("MANGER DES POMMES", 13) == "ZNATRE QRF CBZZRF"
assert chiffrement_cesare("MANGER DES POMMES", -3) == "JXKDBO ABP MLJJBP"        


def chiffrement_vigenère(message, clé):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_chiffré = ""
    masque = []
    m = 0
    for i in clé:
        masque.append(alphabet.index(i))
    for i in range(len(message)):
        if m > len(masque)-1:
            m = 0
        message_chiffré += chiffrement_cesare(message[i],masque[m])
        m+=1
        print(f"masque: {masque}, message: {message_chiffré}")
    return message_chiffré

assert chiffrement_vigenère("J'AI LA CHANCE D'AVOIR DES ELEVES MOTIVES", "NEPASREPETER") == "W'PI CE GAEEPI D'RZDMK URW EDVZTW QFGMKEK"
assert chiffrement_vigenère("MES ELEVES ONT LA CHANCE D'AVOIR UN PROF MOTIVE", "NEPASREPETER") == "ZIH WCIKIL FAX LS GWEGGV H'ANFMG NR CVDF DSIMOI"

            
