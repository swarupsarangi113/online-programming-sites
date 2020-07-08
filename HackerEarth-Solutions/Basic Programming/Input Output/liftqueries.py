#https://github.com/swarup113/HackerEarth-Solutions/new/master/Basic%20Programming/Input%20Output
t = int(input())
lift_position = {'A':0,'B':7}
for _ in range(t) :
    floor = int(input())
    diff_a = abs(floor - lift_position['A'])
    diff_b = abs(floor - lift_position['B'])
    if diff_a <= diff_b :
        print('A')
        lift_position['A'] = floor
    else :
        print('B')
        lift_position['B'] = floor
