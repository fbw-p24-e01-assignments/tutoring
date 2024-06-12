# 1
lst = [59.99, 29.99, 89.50, 45.75, 12.50,
    75.30, 39.99, 65.40, 9.99, 55.00]

def bubble_sort(lst):
    count = 0

    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                count += 1

    return {"lst": lst, "swaps": count}

if __name__ == '__main__':
    bubble = bubble_sort(lst)