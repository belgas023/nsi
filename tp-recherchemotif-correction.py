# Attention : pour bien évaluer la complexité des algorithmes ci-dessous,
# on ne s'autorisera pas à comparer des chaînes de caractères entières (même si Python le permet)
# on les comparera caractère par caractère.

# 1) Commencer par compléter la fonction ci-dessous
# qui effectue la recherche naïve évoquée dans la vidéo
def recherche_naive(texte, motif):
    for position_motif in range(len(texte) - len(motif) + 1):
        index_motif = 0
        while texte[position_motif + index_motif] == motif[index_motif] and index_motif < len(motif) - 1:
            index_motif += 1
        if texte[position_motif + index_motif] == motif[index_motif]:
            return position_motif
    return -1

phrase = "bonjour josianne comment ça va ?"
adn = "CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"

assert recherche_naive(phrase, "comment") == 17
assert recherche_naive(phrase, "coucou") == -1
assert recherche_naive(adn, "CAAGCGCACAAG") == 0
assert recherche_naive(adn, "A") == 1
assert recherche_naive(adn, "AGACGCGGCAGACCT") == 10
assert recherche_naive(adn, "AGGAAGCCAGC") == 340

# 2) Compléter maintenant la fonction ci-dessous qui retourne un dictionnaire
# contenant les décalages à faire comme expliqué dans la vidéo
def décalages(motif):
    dico = {}
    for i in range(len(motif) - 1):
        dico[motif[i]] = len(motif) - i - 1
    return dico
        
assert décalages("comment") == {'c': 6, 'o': 5, 'm': 3, 'e': 2, 'n': 1}
assert décalages("") == {} 
assert décalages("a") == {}
assert décalages("papapa") == {'p': 1, 'a': 2}
assert décalages("quinquennal") == {'q': 6, 'u': 5, 'i': 8, 'n': 2, 'e': 4, 'a': 1}

# 3) Compléter la fonction ci-dessous qui appelle la fonction "décalages"
# et utilise l'algorithme de Boyer-Moore-Horspool expliqué dans la vidéo
def recherche_boyer_moore(texte, motif):
    dico_décalages = décalages(motif)
    position_motif = 0
    while position_motif <= len(texte) - len(motif):
        index_motif = len(motif) - 1
        while texte[position_motif + index_motif] == motif[index_motif] and index_motif > 0:
            index_motif -= 1
        if texte[position_motif + index_motif] == motif[index_motif]:
            return position_motif
        elif texte[position_motif + len(motif) - 1] in dico_décalages:
            position_motif += dico_décalages[texte[position_motif + len(motif) - 1]]
        else:
            position_motif += len(motif)
    return -1
        
assert recherche_boyer_moore(phrase, "comment") == 17
assert recherche_boyer_moore(phrase, "coucou") == -1
assert recherche_boyer_moore(adn, "CAAGCGCACAAG") == 0
assert recherche_boyer_moore(adn, "A") == 1
assert recherche_boyer_moore(adn, "AGACGCGGCAGACCT") == 10
assert recherche_boyer_moore(adn, "AGGAAGCCAGC") == 340


