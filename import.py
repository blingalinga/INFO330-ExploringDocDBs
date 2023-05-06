import sqlite3
from pymongo import MongoClient

# Connect to the SQLite database
conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

# Connect to the MongoDB database
mongo_client = MongoClient()
mongo_db = mongo_client['pokemondb']

# Read data from the SQLite database and transform it into a MongoDB document
for row in c.execute('SELECT p.id, p.pokedex_number, p.name, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, a.name as abilities, GROUP_CONCAT(DISTINCT t.name) as types FROM pokemon AS p LEFT JOIN pokemon_abilities AS pa ON p.id = pa.pokemon_id LEFT JOIN ability AS a ON pa.ability_id = a.id LEFT JOIN pokemon_type AS pt ON p.id = pt.pokemon_id LEFT JOIN type AS t ON pt.type_id = t.id GROUP BY p.id'):
  types_list = [t for t in row[10].split(',') if t]
  doc = {
    'id': row[0],
    'pokedex_number': row[1],
    'name': row[2],
    'hp': row[3],
    'attack': row[4],
    'defense': row[5],
    'speed': row[6],
    'sp_attack': row[7],
    'sp_defense': row[8],
    'types': types_list,
    'abilities': row[9].split(',')
  }

  # Insert the document into the MongoDB database
  mongo_db['pokemon_data'].insert_one(doc)

# Close the connections
conn.close()
mongo_client.close()