"""Get dictionary of word-length: {words}.

Given a phrase, return dictionary keyed by word-length, with the value for
each length being the set of words of that length.

For example::

    >>> answer = word_lengths("cute cats chase fuzzy rats")

This should return {4: {'cute', 'cats'}, 5: {'chase', 'fuzzy', 'rats'}},
but since both dictionaries and sets are unordered, we can't just check if
it matches that exact string, so we'll test more carefully::

    >>> sorted(answer.keys())
    [4, 5]

    >>> answer[4] == {'cute', 'cats', 'rats'}
    True

    >>> answer[5] == {'chase', 'fuzzy'}
    True

Punctuation should be considered part of a word, so you only need to
split the string on whitespace::

    >>> answer = word_lengths("Hi, I'm Balloonicorn")

    >>> sorted(answer.keys())
    [3, 12]

    >>> answer[3] == {'Hi,', "I'm"}
    True

    >>> answer[12] == {"Balloonicorn"}
    True
"""

# make empty dict
# split the string into a list
# loop over each item in list
# len each item and add total as key and word as set value


def word_lengths(sentence):
    """Get dictionary of word-length: {words}."""

    result = {}
    new_phrase = sentence.split(" ")
    
    for item in new_phrase:
        result[len(item)] = set()
        
    for item in new_phrase:
        for key in result.keys():

            if key == len(item):
                result[key].add(item)
            
        
    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NOTHING ESCAPES YOU!\n")
