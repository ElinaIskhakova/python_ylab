def solve(s, word):
    lst = []
    if word == '':
        lst.append(''.rjust(len(s), '-'))
        return lst

    left_s = ''
    for si in range(len(s)):
        if word[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]
            if s[si+1:] == '' and word[1:] == '':
                lst.append(left_s)
            else:
                right_s_list = solve(s[si+1:], word[1:])
                for right_s in right_s_list:
                    lst.append(left_s + right_s)
    return lst 
