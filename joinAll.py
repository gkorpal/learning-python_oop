'''exercise to complete and test this function'''


def joinStrings(stringList):
    '''Join all the strings in stringList into one string,
    and return the result, NOT printing it. For example:

    >>> s = joinStrings(['very', 'hot', 'day']) # returns string
    >>> print(s)
    veryhotday
    '''
    # finish the code for this function
    a = ''
    for b in stringList:
        a = a + b
    return a


def main():
    print(joinStrings(['very', 'hot', 'day']))
    print(joinStrings(['this', 'is', 'it']))
    print(joinStrings(['1', '2', '3', '4', '5']))


main()
