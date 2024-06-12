import pytest
from my_code import bubble_sort

def test_type(): # classes start Test, functions with test_
    assert type(bubble_sort([1, 4, 5])) == dict

def test_swaps():
    bubble = bubble_sort([1, 4, 5])
    swaps = bubble['swaps']
    assert swaps < 30

@pytest.mark.parametrize("cases", [[5, 1, 4],
                                 [-1, -4, 2],
                                 [2, 100, 50]])
def test_right_order(cases):
    bubble = bubble_sort(cases)
    lst = bubble['lst']

    assert lst == sorted(cases)

@pytest.mark.parametrize("cases", [[5, 1, 4],
                                 [-1, -4, 2],
                                 [2, 100, 50]])
def test_wrong_order(cases):
    case_tuple = tuple(cases)
    bubble = bubble_sort(cases)
    lst = bubble['lst']
    truth_lst = list()

    for i in range(len(case_tuple)): # case_tuple (5, 1, 4) # case: 5 > 1 > 4 [4,1,5]
        if lst[i] == case_tuple[i]:
            truth_lst.append(True)
        else:
            truth_lst.append(False)

    assert False in truth_lst
    assert all(truth_lst) == False

@pytest.mark.parametrize("cases,swaps", [([5, 1, 4], 2),
                                 ([-1, -4, 2], 1),
                                 ([2, 100, 50], 1)])
def test_order_and_swaps(cases, swaps):
    bubble = bubble_sort(cases)
    lst = bubble['lst']
    bubble_swaps = bubble['swaps']

    assert lst == sorted(cases)
    assert bubble_swaps == swaps

@pytest.mark.parametrize("cases", [[5, 1, 4],
                                 [-1, -4, 2],
                                 [2, 100, 50]])
def test_swaps(cases):
    bubble = bubble_sort(cases)
    bubble_swaps = bubble['swaps']
    
    if bubble_swaps == 1:
        pytest.fail('evilness')