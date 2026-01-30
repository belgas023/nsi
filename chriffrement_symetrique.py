masque = "CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES"
message_chiffré = []

for i in masque:
    message_chiffré.append(ord(i))

print(message_chiffré)

for i in message_chiffré:
    print(chr(i))
    
def chiffre(message, masque):
    message_crypté = ""
    for i in len(range(message)):
        message_chiffré += ord(message[i]) ^ ord(masque[i])
        