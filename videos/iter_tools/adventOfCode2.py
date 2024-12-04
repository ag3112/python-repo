safe_count = 0
count = 0
with open('/Users/anks/Documents/abc.txt', 'r') as f:
    for line in f:
        count+=1
        lst = list(map(lambda x: int(x), line.rstrip().split(' ')))
        for i in range(0, len(lst)):
            if i == 0:
                safe = True
                typ = 'inc'
            else:
                if num == lst[i]:
                    reason = f'{num} == {lst[i]}'
                    safe = False
                    break
                elif num > lst[i]:
                    if (typ == 'inc') and (i > 1):
                        reason = f'{num}, {lst[i]}, typ {typ} changed'
                        safe = False
                        break
                    else:
                        if (num - lst[i]) <= 3:
                            typ = 'dec'
                        else:
                            reason = f'{num}, {lst[i]}, diff exceed'
                            safe = False
                            break
                else:
                    if (typ == 'dec') and (i > 1):
                        reason = f'{num}, {lst[i]}, typ {typ} changed'
                        safe = False
                        break
                    else:
                        if (lst[i] - num) <= 3:
                            typ = 'inc'
                        else:
                            reason = f'{num}, {lst[i]}, diff exceed'
                            safe = False
                            break
            num = lst[i]
        if safe:
            # print(count)
            safe_count += 1
        else:
            print(line.rstrip())


print(safe_count)
print(count)
