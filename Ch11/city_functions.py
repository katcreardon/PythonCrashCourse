def get_city_name(city, country, population=''):
    """Generate a neatly formatted city and country."""
    if population:
        city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        city_country = city.title() + ', ' + country.title()
    return city_country