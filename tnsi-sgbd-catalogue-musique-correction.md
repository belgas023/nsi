Voici la correction des exercices du fichier `tnsi-sgbd-catalogue-musique.pdf`.

### Page 1

**1) Pourquoi aucune des colonnes ne peut servir de clef primaire ?**

Aucune colonne ne peut servir de clé primaire car aucune ne contient de valeurs uniques pour chaque ligne. Une clé primaire doit identifier de façon unique chaque enregistrement.
- **Titre** : Des morceaux différents peuvent avoir le même titre (par exemple, des reprises comme "Astronomy").
- **Artiste**, **Album**, **Année**, etc. : Ces valeurs apparaissent de multiples fois.

**2) Quel problème va-t-on rencontrer si on veut ajouter des informations sur les artistes (ex: nationalité) ?**

Cela entraînerait de la **redondance de données**. Pour chaque morceau d'un même artiste, il faudrait répéter sa nationalité. Si l'artiste a 100 morceaux, sa nationalité serait stockée 100 fois. Une modification (par exemple, un changement de nationalité) devrait être appliquée sur 100 lignes, ce qui est inefficace et source d'erreurs.

**3) Quel problème va-t-on rencontrer si on souhaite lister tous les morceaux d'un artiste ?**

La colonne `Artiste` contient des chaînes de caractères qui ne sont pas uniformes. Par exemple, pour Metallica, on trouve "Metallica", "Metallica and Marianne Faithfull", et "Metallica and the San Francisco Symphony". Une recherche simple sur le nom "Metallica" ne retournerait pas tous les morceaux sur lesquels le groupe a joué.

**4) Pourquoi la nouvelle représentation ne permet toujours pas de gérer les morceaux faits par plusieurs artistes ?**

Le schéma `Morceau(..., artiste_id, ...)` et `Artiste(artiste_id, nom)` ne règle pas le problème car la table `Morceau` ne possède qu'un seul champ `artiste_id`. Un morceau ne peut donc être associé qu'à un seul artiste. Pour une collaboration comme "Under Pressure" par Queen et David Bowie, on ne pourrait attribuer le morceau qu'à l'un des deux, pas aux deux.

---

### Page 2

**5) Compléter les tables Morceau, Interprete et Artiste.**

L'exercice consiste à normaliser les données. Voici une proposition de remplissage basée sur les informations du premier tableau et les identifiants de l'énoncé.

**Table `Artiste`**
| artiste_id | nom |
|---|---|
| 25 | Blue Öyster Cult |
| 79 | Queen |
| 108 | David Bowie |
| 154 | Metallica |
| 318 | Marianne Faithfull |

**Table `Morceau`**
| titre_id | titre | duree |
|---|---|---|
| 519 | Astronomy | 384 |
| 1219 | Astronomy | 398 |
| 316 | Stone Cold Crazy | 136 |
| 1319 | Stone Cold Crazy | 139 |
| 1298 | Fuel | 270 |
| 1570 | The Memory Remains| 279 |
| 401 | Under Pressure | 242 |
| 1125 | The Outlaw Torn | 589 |
| 1591 | The Outlaw Torn | 599 |

**Table `Interprete`**
| titre_id | artiste_id |
|---|---|
| 519 | 25 |
| 1219 | 154 |
| 316 | 79 |
| 1319 | 154 |
| 1298 | 154 |
| 1570 | 154 |
| 1570 | 318 |
| 401 | 79 |
| 401 | 108 |
| 1125 | 154 |
| 1591 | 154 |

**6) Comment appelle-t-on les clefs de certaines tables comme Interprete dont les valeurs sont définies dans d'autres tables ?**

Ce sont des **clés étrangères** (en anglais, *Foreign Keys*).

**7) Expliquer pourquoi le couple (titre_id, artiste_id) peut servir de clef primaire à Interprete.**

Ce couple est unique pour chaque ligne de la table `Interprete`. Il représente le fait qu'un artiste (`artiste_id`) interprète un morceau (`titre_id`). Un artiste n'interprète pas "deux fois" le même morceau (dans ce contexte), et un morceau peut être interprété par plusieurs artistes, ce qui crée plusieurs lignes avec le même `titre_id` mais des `artiste_id` différents. La combinaison des deux est donc unique.

**8) Traduire en langage naturel les requêtes suivantes :**

- **Requête 1** : Sélectionne le titre et la durée des morceaux qui durent plus de 600 secondes, et les affiche en les triant par durée, de la plus longue à la plus courte.
- **Requête 2** : Sélectionne le numéro de CD, le numéro de piste et le titre des morceaux de l'album "Garage Inc.", triés par numéro de CD puis par numéro de piste.

**9) Donner les requêtes SQL permettant d'obtenir les résultats suivants :**

a) `SELECT nom FROM Artiste WHERE artiste_id = 200;`
b) `SELECT nom FROM Album WHERE annee BETWEEN 1999 AND 2010;`
c) `SELECT m.titre, m.duree FROM Morceau m JOIN Interprete i ON m.titre_id = i.titre_id WHERE i.artiste_id = 200 ORDER BY m.duree DESC;`

**10) Donner la requête permettant à 'Maître Gims' de devenir 'Gims' dans la table des artistes.**

`UPDATE Artiste SET nom = 'Gims' WHERE nom = 'Maître Gims';`

---

### Page 3

**11) Expliquer pourquoi le couple (titre_id, util_id) ne peut pas être une clef primaire de la table Ecoute.**

Un utilisateur peut écouter le même morceau plusieurs fois. Le couple (`titre_id`, `util_id`) ne serait donc pas unique pour chaque écoute. Une clé primaire doit garantir l'unicité de chaque ligne. C'est le rôle de `id_ecoute`.

**12) Donner la requête SQL permettant d'ajouter l'utilisateur numéro 2179.**

```sql
INSERT INTO Utilisateur (util_id, nom, e-mail, adresse)
VALUES (2179, 'Bob VHS', 'bob.vhs@hotmail.com', 'New York');
```

**13) Traduire la requête suivante en langage naturel :**

"Compter le nombre de titres de morceaux distincts écoutés le 12 décembre 2020."

**14) Écrire une requête qui permette d'obtenir un affichage le plus proche possible du tableau présenté en tout début de TP.**

Pour recréer la table initiale, il faut joindre plusieurs tables et agréger les noms des artistes pour les collaborations.

```sql
SELECT
    m.titre AS "Titre",
    m.duree AS "Durée",
    GROUP_CONCAT(a.nom, ' and ') AS "Artiste",
    al.nom AS "Album",
    c.piste AS "Piste",
    c.cd AS "CD",
    al.annee AS "Année"
FROM
    Morceau AS m
JOIN
    Interprete AS i ON m.titre_id = i.titre_id
JOIN
    Artiste AS a ON i.artiste_id = a.artiste_id
JOIN
    Contient AS c ON m.titre_id = c.titre_id
JOIN
    Album AS al ON c.album_id = al.album_id
GROUP BY
    m.titre_id
ORDER BY
    al.annee;
```
*Note : La fonction `GROUP_CONCAT` est spécifique à certains systèmes de bases de données comme SQLite et MySQL. Elle permet de concaténer les noms d'artistes pour un même morceau.*