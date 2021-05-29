def find_farthest_orbit(list_of_orbits):
    maximum = (0, -1, -1)
    without_rounds = [i for i in list_of_orbits if i[0] != i[1]]
    for i in without_rounds:
        if int(i[0]) * int(i[1]) > maximum[0]:
            maximum = int(i[0]) * int(i[1]), i[0], i[1]
    answer = maximum[1], maximum[2]
    return answer


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))