def egg_count(display):
    count = 0
    while display > 0:
        if display % 2 == 1:
            count += 1
        display = display // 2
    return count