from artsango_ai import (
    generer_bio,
    generer_description_produit,
    generer_post_reseaux,
    generer_storytelling,
    assistant_artisan
)

print("=" * 50)
print("TEST 1 — Bio d'artisan")
print("=" * 50)
bio = generer_bio(
    nom="Kofi Mensah",
    metier="Sculpteur sur bois",
    ville="Abomey",
    annees_experience=15
)
print(bio)

print("\n" + "=" * 50)
print("TEST 2 — Description produit")
print("=" * 50)
description = generer_description_produit(
    nom_produit="Masque Fon traditionnel",
    materiaux="Bois d'iroko, pigments naturels",
    origine="Abomey, Bénin",
    prix=25000
)
print(description)

print("\n" + "=" * 50)
print("TEST 3 — Post Instagram")
print("=" * 50)
post = generer_post_reseaux(
    produit="Collier en bronze fait à la main, motifs Yoruba"
)
print(post)

print("\n" + "=" * 50)
print("TEST 4 — Conversation avec l'assistant")
print("=" * 50)

# Conversation avec mémoire
historique = []

question1 = "Bonjour, je suis tisserand et je veux vendre mes pagnes en ligne."
reponse1 = assistant_artisan(question1)
print(f"Vous : {question1}")
print(f"ArtSango AI : {reponse1}")

# Ajouter à l'historique pour garder le contexte
historique.append({"role": "user", "content": question1})
historique.append({"role": "assistant", "content": reponse1})

question2 = "Par où je dois commencer ?"
reponse2 = assistant_artisan(question2, historique=historique)
print(f"\nVous : {question2}")
print(f"ArtSango AI : {reponse2}")
try:
    bio = generer_bio("Kofi", "Sculpteur", "Abomey", 15)
    print(bio)
except Exception as e:
    print(f"Erreur après plusieurs tentatives : {e}")