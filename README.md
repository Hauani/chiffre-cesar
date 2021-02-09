### Projet d'introduction à Github (chiffre de César                                                                                                                                               #### 1. Le chiffre 

#### 1. Le chiffre de César
Le chiffre de César est une méthode de chiffrement très simple utilisée par Jules César dans ses correpondances secrètes. Pour obtenir le texte chiffré, on remplace simplement chaque lettre du texte en clair par la lettre qui se trouve trois place plus loin dans l'alphabet "modulo 26". Ainsi, A est remplacé par D, B par E, W par Z, X par A etc. On utilise parfois un décalage autre que 3.

#### 2. Implémentation
Dans ce projet, on écrira :
- une fonction '''chiffrement(message)''' qui permet de chiffrer une chaîne de caractères (écrits en capitales) ;
- une fonction '''dechiffrement(message_chiffre)''' qui permet de déchiffrer une chaîne de caractères (écrits en capitales) ;
- une fonction principale qui demande à l'utilisateur de choisir entre chiffrement et déchiffrement, avant de lui demander le texte (à chiffrer ou déchiffrer).

#### 3. Fichiers
Il faudra donc créer tris fichiers : un fichier '''chiffrement.py''', un fichier '''dechifffrement.py''' et un fichier '''main.py'''.