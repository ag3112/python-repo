def get_longest_substring(s):
    sub_string = ''
    max_sub_string = ''
    for x in range(0, len(s)):
        if x == 0:
            sub_string = s[x]
            max_sub_string = sub_string
        else:
            if s[x] in sub_string:
                if len(max_sub_string) < len(sub_string):
                    max_sub_string = sub_string

                if sub_string[-1] == s[x]:
                    sub_string = s[x]
                else:
                    sub_string = sub_string[sub_string.index(s[x])+1:] + s[x]
            else:
                sub_string = sub_string + s[x]
                if len(max_sub_string) < len(sub_string):
                    max_sub_string = sub_string

    return max_sub_string


if __name__ == '__main__':
    s = 'anviaj'
    result = get_longest_substring(s)
    print(f'{result} is the longest string in {s} and have length {len(result)}')
