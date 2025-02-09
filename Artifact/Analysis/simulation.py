import random
from datetime import timedelta, datetime

simulated_names = [
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

user_data = {}

unhappy = ["Happy"] * 10 + ["OK"] * 25 + ["Sad"] * 35
happy = ["Happy"] * 35 + ["OK"] * 25 + ["Sad"] * 10

current_time = datetime.now()

with open("data.csv", "a") as simulation_file:
    for _ in range(10000):
        name = random.choice(simulated_names)

        # Initialize user data if not present
        if name not in user_data:
            user_data[name] = {"ShotsTaken": random.randint(20, 100), "ShotsScored": random.randint(0, 14)}

        else:
            # Update user data and simulate linear improvement in accuracy
            user_data[name]["ShotsTaken"] += 1
            improvement_factor = 0.02  # Adjust this factor for desired linearity
            user_data[name]["ShotsScored"] += max(1, round(user_data[name]["ShotsTaken"] * improvement_factor))

        happiness_before = random.choice(unhappy)
        happiness_after = random.choice(happy)
        start_time = current_time - timedelta(days=random.randint(1, 7), minutes=random.randint(0, 1439))

        shots_taken = random.randint(1, 200)

        # Simulate improvement in shooting accuracy over time
        shots_scored = max(user_data[name]["ShotsScored"], random.randint(round(0.2 * shots_taken), shots_taken))
        if shots_scored > shots_taken:
            shots_scored = shots_taken - random.randint(0,round(0.1 * shots_taken))
        end_time = start_time + timedelta(minutes=random.randint(3, 40), seconds=random.randint(0, 60))

        out_str = f"{name}, {happiness_before}, {start_time.strftime('%Y-%m-%d %H:%M')}, {happiness_after}, {shots_taken}, {shots_scored}, {end_time.strftime('%Y-%m-%d %H:%M')}\n"
        simulation_file.write(out_str)
