def freq_counter(coll):
    """Return frequency counter of a collection
    
        >>> freq_counter([1, 2, 3, 4, 4, 4])
        {1: 1, 2: 1, 3: 1, 4: 3}
        
        >>> freq_counter('abcc')
        {'a': 1, 'b': 1, 'c': 2}
    """
    freq = {}
    for item in coll:
        freq[item] = freq.get(item, 0) + 1
    return freq

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return freq_counter(str(num1)) == freq_counter(str(num2))