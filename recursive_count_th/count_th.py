'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if len(word) < 2:
        return 0

    # isTh = 0

    # if word[:2] == 'th':
    #     isTh = 1

    # return isTh + count_th(word[1:])

    return (1 if word[:2] == 'th' else 0) + count_th(word[1:])