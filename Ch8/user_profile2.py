# The double ** creates an empty dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('kathryn', 'reardon',
                             location='greensboro',
                             field='computer science',
                             marital_status='married')
print(user_profile)