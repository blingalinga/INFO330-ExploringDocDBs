# Write a query that returns all the Pokemon with an attack greater than 150

from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Find all documents where the attack field is greater than 150
high_attack_pokemon = pokemonColl.find({"attack": {"$gt": 150}})

# Print each document
for high_attack in high_attack_pokemon:
    print(high_attack)