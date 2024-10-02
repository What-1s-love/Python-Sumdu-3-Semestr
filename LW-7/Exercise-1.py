def display_all_countries(countries):
    """
    Displays all country data in the dictionary.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    print("\nAll Countries Data:")
    print("{:<15} {:<20} {:<20}".format("Country", "Population (M)", "Area (K sq km)"))
    print("-" * 55)
    for country, data in countries.items():
        print("{:<15} {:<20} {:<20}".format(country, data['population'], data['area']))


def add_country(countries):
    """
    Adds a new country to the dictionary.
    """
    try:
        name = input("\nEnter the country name: ").strip()
        if not name:
            print("Country name cannot be empty.")
            return
        if name in countries:
            print(f"Country '{name}' already exists in the dictionary.")
            return
        population = float(input("Enter the population (in millions): "))
        if population < 0:
            print("Population cannot be negative.")
            return
        area = float(input("Enter the area (in thousands of sq km): "))
        if area <= 0:
            print("Area must be greater than zero.")
            return
        countries[name] = {'population': population, 'area': area}
        print(f"Country '{name}' has been added successfully.")
    except ValueError:
        print("Invalid input. Please enter numerical values for population and area.")


def remove_country(countries):
    """
    Removes a country from the dictionary.
    """
    name = input("\nEnter the country name to remove: ").strip()
    try:
        del countries[name]
        print(f"Country '{name}' has been removed successfully.")
    except KeyError:
        print(f"Country '{name}' does not exist in the dictionary.")


def display_sorted_countries(countries):
    """
    Displays countries sorted by their names.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    sorted_countries = sorted(countries.keys())
    print("\nCountries Sorted by Name:")
    print("{:<15} {:<20} {:<20}".format("Country", "Population (M)", "Area (K sq km)"))
    print("-" * 55)
    for country in sorted_countries:
        data = countries[country]
        print("{:<15} {:<20} {:<20}".format(country, data['population'], data['area']))


def find_max_density_country(countries):
    """
    Finds and displays the country with the highest population density.
    """
    if not countries:
        print("\nThe country dictionary is empty.")
        return
    max_density = None
    max_density_country = None
    for country, data in countries.items():
        density = data['population'] / data['area']
        if (max_density is None) or (density > max_density):
            max_density = density
            max_density_country = country
    print("\nCountry with the Highest Population Density:")
    print(f"{max_density_country} with a density of {max_density:.2f} million per thousand sq km.")


def initialize_countries():
    """
    Initializes the country dictionary with predefined data.
    """
    return {
        'CountryA': {'population': 50.0, 'area': 25.0},
        'CountryB': {'population': 80.0, 'area': 40.0},
        'CountryC': {'population': 30.0, 'area': 15.0},
        'CountryD': {'population': 60.0, 'area': 30.0},
        'CountryE': {'population': 90.0, 'area': 45.0},
        'CountryF': {'population': 70.0, 'area': 35.0},
        'CountryG': {'population': 20.0, 'area': 10.0},
        'CountryH': {'population': 40.0, 'area': 20.0},
        'CountryI': {'population': 100.0, 'area': 50.0},
        'CountryJ': {'population': 55.0, 'area': 27.5},
    }


def get_country_data(num_countries):
    """
    Collects data for a specified number of countries from the user.
    """
    countries = {}
    for i in range(1, num_countries + 1):
        print(f"\nEnter details for country #{i}:")
        name = input("Country Name: ").strip()
        if not name:
            print("Country name cannot be empty. Skipping this entry.")
            continue
        if name in countries:
            print(f"Country '{name}' already exists. Skipping duplicate entry.")
            continue

        while True:
            try:
                population = float(input("Population (in millions): "))
                if population < 0:
                    print("Population cannot be negative. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for population.")
        
        while True:
            try:
                area = float(input("Area (in thousands of square km): "))
                if area <= 0:
                    print("Area must be greater than zero. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for area.")
        
        density = population / area
        countries[name] = {'population': population, 'area': area, 'density': density}
        print(f"Country '{name}' added successfully with a density of {density:.2f} million per thousand sq km.")
    return countries

"""
Main function to run the country data management program.
"""
countries = initialize_countries()
while True:
    print("\n=== Country Data Management ===")
    print("1. Display all countries")
    print("2. Add a new country")
    print("3. Remove a country")
    print("4. Display countries sorted by name")
    print("5. Find country with highest population density")
    print("6. Enter data for new countries")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ").strip()

    if choice == '1':
        display_all_countries(countries)
    elif choice == '2':
        add_country(countries)
    elif choice == '3':
        remove_country(countries)
    elif choice == '4':
        display_sorted_countries(countries)
    elif choice == '5':
        find_max_density_country(countries)
    elif choice == '6':
        try:
            num_countries = int(input("\nHow many countries would you like to add? "))
            if num_countries <= 0:
                print("Number of countries must be positive.")
                continue
            new_countries = get_country_data(num_countries)
            countries.update(new_countries)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
