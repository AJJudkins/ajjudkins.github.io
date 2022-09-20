import random


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 1:
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 2:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity, preposition):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        determiner = get_determiner(quantity=1)
        noun = get_noun(quantity=1)
    else:
        determiner = get_determiner(quantity=2)
        noun = get_noun(quantity=2)

    prepositional_phrase = (f"{preposition} {determiner} {noun}")

    return prepositional_phrase


def main():
    past = 1
    present = 2

    """Single Past"""
    single_past_determiner = get_determiner(quantity=1)
    single_past_noun = get_noun(quantity=1)
    single_past_verb = get_verb(quantity=1, tense=past)
    single_past_preposition = get_preposition()
    single_past_phrase = get_prepositional_phrase(
        quantity=1, preposition=single_past_preposition)
    print(
        f"a. {single_past_determiner.capitalize()} {single_past_noun} {single_past_verb} {single_past_phrase}.")

    """Single Present"""
    single_present_determiner = get_determiner(quantity=1)
    single_present_noun = get_noun(quantity=1)
    single_present_verb = get_verb(quantity=1, tense=present)
    single_present_preposition = get_preposition()
    single_present_phrase = get_prepositional_phrase(
        quantity=1, preposition=single_present_preposition)
    print(f"b. {single_present_determiner.capitalize()} {single_present_noun} {single_present_verb} {single_present_phrase}.")

    """Single Future"""
    single_future_determiner = get_determiner(quantity=1)
    single_future_noun = get_noun(quantity=1)
    single_future_verb = get_verb(quantity=1, tense=0)
    single_future_preposition = get_preposition()
    single_future_phrase = get_prepositional_phrase(
        quantity=1, preposition=single_future_preposition)
    print(
        f"c. {single_future_determiner.capitalize()} {single_future_noun} {single_future_verb} {single_future_phrase}.")

    """Plural Past"""
    plural_past_determiner = get_determiner(quantity=2)
    plural_past_noun = get_noun(quantity=2)
    plural_past_verb = get_verb(quantity=2, tense=past)
    plural_past_preposition = get_preposition()
    plural_past_phrase = get_prepositional_phrase(
        quantity=2, preposition=plural_past_preposition)
    print(
        f"d. {plural_past_determiner.capitalize()} {plural_past_noun} {plural_past_verb} {plural_past_phrase}.")

    """Plural Present"""
    plural_present_determiner = get_determiner(quantity=2)
    plural_present_noun = get_noun(quantity=2)
    plural_present_verb = get_verb(quantity=2, tense=present)
    plural_present_preposition = get_preposition()
    plural_present_phrase = get_prepositional_phrase(
        quantity=2, preposition=plural_present_preposition)
    print(f"e. {plural_present_determiner.capitalize()} {plural_present_noun} {plural_present_verb} {plural_present_phrase}.")

    """Plural Future"""
    plural_future_determiner = get_determiner(quantity=2)
    plural_future_noun = get_noun(quantity=2)
    plural_future_verb = get_verb(quantity=2, tense=0)
    plural_future_preposition = get_preposition()
    plural_future_phrase = get_prepositional_phrase(
        quantity=2, preposition=plural_future_preposition)
    print(
        f"f. {plural_future_determiner.capitalize()} {plural_future_noun} {plural_future_verb} {plural_future_phrase}.")


main()
