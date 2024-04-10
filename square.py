from itertools import permutations
def telephone_words(digit_string):
    spisok = []
    result_spisok = []
    d = {'0': '0','1': '1','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno','7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    for i in range(len(digit_string)):
        if i == 0:
            for letter in d[digit_string[i]]:
                spisok.append(letter)
        else:
            result_spisok = []
            for elem in spisok:
                for letter in d[digit_string[i]]:
                    result_spisok.append((elem + letter).upper())
            spisok = result_spisok

    return spisok

telephone_words("1234")