# import os

# # Define the directory and the list of file names
# directory = "data/html/centrafrique.sango.free.fr"
# filenames = [
#     "transport.html",
#     "poste.html",
#     "geographie.html",
#     "climat.html",
#     "nature.html",
#     "animaux.html",
#     "aliments.html",
#     "fruits_legumes.html",
#     "corps.html",
#     "habits.html",
#     "sport.html",
#     "nombres.html",
#     "couleurs.html",
#     "temps.html",
#     "jours.html",
#     "mois.html",
#     "pronoms.html",
#     "questions.html",
# ]

# # Create the directory if it doesn't exist
# os.makedirs(directory, exist_ok=True)

# # Create each file
# for filename in filenames:
#     with open(os.path.join(directory, filename), 'w') as f:
#         f.write("""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document Title</title>
# </head>
# <body>
#     <h1>Welcome to My Website</h1>
#     <p>This is a basic HTML template.</p>
# </body>
# </html>
#         """)

import os
import json

# Define the directory and the list of file names
directory = "data/json"
filenames = [
    "salutations.json",
    "famille.json",
    "maison.json",
    "ville.json",
    "transport.json",
    "Poste.json",
    "geographie.json",
    "climat.json",
    "nature.json",
    "animaux.json",
    "aliments.json",
    "fruits_legumes.json",
    "corps.json",
    "habits.json",
    "sport.json",
    "nombres.json",
    "couleurs.json",
    "temps.json",
    "jours.json",
    "mois.json",
    "pronoms.json",
    "questions.json",
]

# Create the directory if doesn't exist
os.makedirs(directory, exist_ok=True)

# Create each file
for filename in filenames:
    with open(os.path.join(directory, filename), 'w') as f:
        json.dump({}, f)