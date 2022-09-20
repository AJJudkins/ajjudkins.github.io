from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):

        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        word = get_noun(2)
        assert word in plural_nouns


def test_get_verb():

    single_past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                         "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1, 1)
        assert word in single_past_verbs

    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(1, 2)
        assert word in single_present_verbs

    single_future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                           "will think", "will run", "will sleep", "will talk",
                           "will walk", "will write"]

    for _ in range(4):
        word = get_verb(1, 3)
        assert word in single_future_verbs

    plural_past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                         "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(2, 1)
        assert word in plural_past_verbs

    plural_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                            "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(2, 2)
        assert word in plural_present_verbs

    plural_future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                           "will think", "will run", "will sleep", "will talk",
                           "will walk", "will write"]

    for _ in range(4):
        word = get_verb(2, 3)
        assert word in plural_future_verbs


def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in prepositions

    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):

        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        word = get_noun(2)
        assert word in plural_nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
