"""Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you. """


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


steven = build_profile('steven', 'nodalo', age=34, marital_status='married', kin=1)

[print(f"{key.title()}: {value}") for key, value in steven.items()]