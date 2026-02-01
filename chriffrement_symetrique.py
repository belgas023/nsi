masque = "CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES"
message = "Message secret"    

def chiffre(message, masque):
    message_crypté = [] 
    for i in range(len(message)):
        message_crypté.append(ord(message[i]) ^ ord(masque[i]))
    return message_crypté

def dechiffre(message, masque):
    message_decrypté = ""
    for i in range(len(message)):
        message_decrypté += chr( message[i] ^ ord(masque[i]) )
    return message_decrypté
         

print(chiffre(message, masque))
print(dechiffre( chiffre(message, masque) , masque))
