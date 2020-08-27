def search4vowels(phrase) -> set:
    """Возвращает гласные, найденые в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'letters' , найденых в указанной фразе."""
    return set(letters).intersection(set(phrase))
