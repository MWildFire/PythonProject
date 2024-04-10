def strip_comments_old(strng, markers):
    for elem in markers:
        while elem in strng:
            marker_ind = strng.find(elem) # 12
            next_line_ind = strng[marker_ind:].find('\n') # 13
            strng = strng[:marker_ind-1] + strng[marker_ind:][next_line_ind:]
    return strng


strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])


