# Write a query that returns all the Pokemon with an ability of "Overgrow"

from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

overgrow_pokemon = pokemonColl.find({"abilities": {"$regex": ".*Overgrow.*"}})

# Print each document
for pokemon in overgrow_pokemon:
    print(pokemon)