#Simple, given a string of words, return the length of the shortest word(s).
#
#String will never be empty and you do not need to account for different data types.


def find_short(s):
    new_list = list(s.split())
    l = len(new_list[0])
    for i in range(len(new_list)):
        if len(new_list[i]) < l:
            l = i
    return l
