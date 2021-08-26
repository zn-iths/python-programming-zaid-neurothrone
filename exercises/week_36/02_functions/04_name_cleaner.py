def name_cleaner(name: str) -> str:
    """
    Returns a name stripped from leading and trailing blank
    spaces, all first letters of each word capitalized and the
    rest lowercase.
    """
    return name.strip().lower().title()


print(name_cleaner("johnny bravo"))
print(name_cleaner("  JohnnY bRaVo    "))
