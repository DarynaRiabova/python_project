
def common_elements():
    range_three = {i for i in range(100) if i % 3 == 0}
    range_five = {i for i in range(100) if i % 5 == 0}

    return range_three & range_five
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
