#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#Examples:
#
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    str = text.split()
    for i in range(len(str)):
        if str[i] in '!.?%&':
            continue
        else:
            str[i] = str[i][1:] + str[i][0] + 'ay'
    return " ".join(str)
