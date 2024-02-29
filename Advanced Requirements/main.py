import csv

def get_life_expectancy(country):
    with open('Life_expectancy_dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Country'] == country:
                return float(row['Overall Life'])

def main():
    country = input("Enter your country: ").title()
    while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("ERROR: Please enter a number for age")
        else:
            break
    life_expectancy = get_life_expectancy(country)

    if life_expectancy:
        remaining_years = life_expectancy - age
        continent = get_continent(country)
        print(f"You live in {country} which is in {continent}. Based on your current age {age}, you will live another {remaining_years:.2f} years.")
    else:
        print(f"ERROR: {country} is not a Valid Country, Please Try Again.")

def get_continent(country):
    with open('Life_expectancy_dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Country'] == country:
                return row['Continent']

if __name__ == "__main__":
    main()
