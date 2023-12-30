def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s

    if s == s[::-1]:
        return s
    #
    # l_idx = 0
    # r_idx = -1
    #
    # p = ''
    # while True:
    #     f_ele = s[l_idx]
    #     r_str = s[l_idx+1:]
    #     if s[l_idx:r_idx] == s[l_idx:r_idx:-1]:
    #         l = s[l_idx:r_idx]
    #         if len(p) < len(l):
    #             p = l
    #     else:
    #
    # return p



if __name__ == '__main__':
    x = longestPalindrome('aacabdkacaa')
    print(x)
