def get_country_data(num_countries):
    countries = []
    for i in range(1, num_countries + 1):
        print(f"\nEnter details for country #{i}:")
        name = input("Country Name: ").strip()

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
        countries.append({
            'name': name,
            'population': population,
            'area': area,
            'density': density
        })
    return countries

def find_country_with_max_density(countries):
    if not countries:
        return None
    max_density_country = countries[0]
    for country in countries[1:]:
        if country['density'] > max_density_country['density']:
            max_density_country = country
    return max_density_country

num_countries = 10
print("=== Population Density Calculator ===")
countries = get_country_data(num_countries)
    
max_density_country = find_country_with_max_density(countries)
    
if max_density_country:
    print("\nCountry with the highest population density:")
    print(f"Name: {max_density_country['name']}")
    print(f"Population: {max_density_country['population']} million")
    print(f"Area: {max_density_country['area']} thousand sq km")
    print(f"Density: {max_density_country['density']:.2f} million per thousand sq km")
else:
    print("No country data available.")