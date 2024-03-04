# Generate fake data for Shooting data
import random
from datetime import timedelta, datetime


fake_names  = [
    'Sean', 'Aoife', 'Cian', 'Saoirse', 'Niall', 'Ciara', 'Eoin', 'Roisin', 'Padraig', 'Siobhan',
    'Conor', 'Maeve', 'Fionn', 'Orla', 'Liam', 'Niamh', 'Cillian', 'Grainne', 'Darragh', 'Aoibhinn',
    'Ciaran', 'Fiona', 'Cathal', 'Mairead', 'Cormac', 'Deirdre', 'Odhran', 'Aisling', 'Ronan', 'Aine',
    'Donal', 'Brigid', 'Brendan', 'Sinead', 'Ruairi', 'Maura', 'Diarmuid', 'Eimear', 'Eoghan', 'Treasa',
    'Oisin', 'Clodagh', 'Tadhg', 'Nuala', 'Fergus', 'Sorcha', 'Caoimhe', 'Orlaith', 'Ciar', 'Sorcha',
    'Dara', 'Aoibheann', 'Rory', 'Mairin', 'Colm', 'Blathnaid', 'Tomas', 'Clare', 'Caoilfhionn', 'Cian',
    'Aoibhe', 'Seanan', 'Siofra', 'Cillian', 'Fainche', 'Daire', 'Riona', 'Lorcan', 'Muireann', 'Peadar',
    'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Jackson', 'Lucas', 'Aiden',
    'Oliver', 'Elijah', 'Charlotte', 'Mia', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Ella',
    'Benjamin', 'Henry', 'Alexander', 'Sebastian', 'James', 'Joseph', 'Samuel', 'Daniel', 'Matthew', 'David',
    'Grace', 'Chloe', 'Zoe', 'Lily', 'Layla', 'Aria', 'Mila', 'Scarlett', 'Penelope', 'Sofia',
    'Landon', 'Carter', 'Ethan', 'Michael', 'Logan', 'Mason', 'Caleb', 'Daniel', 'Eli', 'Wyatt',
    'Avery', 'Ella', 'Madison', 'Scarlett', 'Grace', 'Victoria', 'Hannah', 'Eleanor', 'Nora', 'Lillian'
]

# 2 Weighted datasets
unhappy = ["Happy"] * 10 + ["OK"] * 25 + ["Sad"] * 35

happy = ["Happy"] * 35 + ["OK"] * 25 + ["Sad"] * 10

current_time = datetime.now()

with open("fake.csv", "a") as fake_file:
    for _ in range(10000):
        name = random.choice(fake_names)
        happiness_before = random.choice(unhappy)
        happiness_after = random.choice(happy)
        start_time = current_time - timedelta(days=random.randint(1, 7), minutes=random.randint(0, 1439))

        shots_taken = random.randint(1, 10)
        shots_scored = random.randint(0, shots_taken)
        end_time = start_time + timedelta(minutes=random.randint(3, 40), seconds=random.randint(0,60))

        out_str = f"{name}, {happiness_before}, {start_time.strftime("%Y-%m-%d %H:%M")}, {happiness_after}, {shots_taken}, {shots_scored}, {end_time.strftime("%Y-%m-%d %H:%M")}\n"
        fake_file.write(out_str)