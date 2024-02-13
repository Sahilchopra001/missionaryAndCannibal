def solve():
    print("Given we have 3 cannibals and 3 missionaries who have to cross the river")
    boat = 0
    can_at_start = 3
    can_at_end = 0
    mis_at_start = 3
    mis_at_end = 0
    print("\nNumber of cannibles at start : ", can_at_start)
    print("Number of missionaries at start : ", mis_at_start)
    print("Number of cannibles at end : ", can_at_end)
    print("Number of missionaries at end : ", mis_at_end)
    while mis_at_end != 3 or can_at_end != 3:
        if boat == 0:
            boat = 1
            if can_at_start >= 2 and mis_at_start != 2:
                print("\nboat will take 2 cannibles to end")
                can_at_end += 2
                can_at_start -= 2
            else:
                print("\nboat will take 2 missionaries to end")
                mis_at_end += 2
                mis_at_start -= 2
        else:
            boat = 0
            if mis_at_end == 2:
                print("\nboat will take 1 cannible and 1 missionary to start")
                mis_at_end -= 1
                can_at_end -= 1
                can_at_start += 1
                mis_at_start += 1
            else:
                print("\nboat will take 1 cannible to start")
                can_at_end -= 1
                can_at_start += 1
        print("\nNumber of cannibles at start : ", can_at_start)
        print("Number of missionaries at start : ", mis_at_start)
        print("Number of cannibles at end : ", can_at_end)
        print("Number of missionaries at end : ", mis_at_end)


solve()



