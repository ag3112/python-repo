def binary_search(li, key):
    start = 0
    end = len(li) - 1

    while start <= end:

        mid = (start + end) // 2
        if key == li[mid]:
            return mid
        elif key < li[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    key = 91
    found = binary_search(l, key)
    if found != -1:
        print(f'{key} found at index {found} in list {l}')
    else:
        print(f'{key} is not present in list {l}')
