cities = {
        'greensboro': {
                'country': 'USA',
                'population': 290222,
                'fact': 'Greensboro was the site of the Woolworth sit-ins.',
                },
        'tokyo': {
                'country': 'Japan',
                'population': 9273000,
                'fact': "Tokyo is Japan's most populous city.",
                },
        'cairo': {
                'country': 'Egypt',
                'population': 9500000,
                'fact': 'Cairo is the location of the pyramids and' + 
                ' Great Sphinx.',
                },                
        }

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry: " + city_info['country'])
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'])