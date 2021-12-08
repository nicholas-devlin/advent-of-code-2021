with open('input.txt') as f:
    previous = int(f.readline())
    count = 0
    increasing_measurements = 0
    print(previous)
    for line in f:
        # if count > 5:
        #     break
        
        current = int(line)
        if current > previous:
            increasing_measurements += 1
        previous = current
        print(previous)
        count += 1

print(increasing_measurements)