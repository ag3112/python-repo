class Solution:
    def compress(self, chars) -> int:

        if len(chars) == 1:
            return 1

        lchar = chars[-1]
        idx2pop = -1
        ccounter = 0
        idx = -1
        while True:
            cchar = chars.pop(idx2pop)
            if lchar == cchar:
                ccounter += 1
                if idx2pop != -1:
                    pass
                else:
                    idx2pop = -1
            else:
                if idx2pop == -1:
                    chars.append(cchar)
                    chars.append(lchar)
                    chars.append(ccounter)
                    
                else:
                    chars.insert(idx2pop, cchar)
                    chars.insert(idx2pop + 1, lchar)
                    chars.insert(idx2pop + 1, ccounter)

                lchar = cchar
                idx2pop = idx + ccounter - 2
                ccounter = 0

            idx -= 1
            if idx == -25:
                break


        print(chars)


if __name__ == '__main__':
    s = Solution()
    s.compress(["a","a","b","b","c","c","c"])