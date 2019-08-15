def binary_search(sets, update_list):
    update_list.sort()
    find = []
    n = 0
    ans = 'no'
    while n < len(sets):
        first = 0
        last = len(update_list)
        while first <= last and ans == 'no':
            mid = int((first+last) / 2)
            if update_list[mid] == sets[n]:
                find.append(update_list[mid])
                ans = 'yes'
            elif update_list[mid] < sets[n]:
                first = mid + 1
            else:
                last = mid - 1
        # If we reach here, then the element was not present
        n += 1
        ans = 'no'
    return find