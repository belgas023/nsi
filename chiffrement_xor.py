def chiffrement_xor(message, clé):
    message_chiffré = []
    for i in range(len(message)):
        message_chiffré.append(ord(message[i]) ^ ord(clé[i]))
    return message_chiffré

message = "Un message bien énigmatique !"
clé = "Les sanglots longs des violons de l'automne blessent mon coeur d'une langueur monotone."
assert chiffrement_xor(message, clé) == [25,11,83,77,22,18,29,6,11,10,84,17,73,9,1,78,142,29,73,3,8,18,84,31,24,26,9,79,79]
