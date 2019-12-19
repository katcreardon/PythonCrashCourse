def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    info = {}
    info['manufacturer'] = manufacturer
    info['model'] = model
    for key, value in car_info.items():
        info[key] = value
    return info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)