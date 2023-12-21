def dynamic_construct_rocket(rocket_sections, target_length):
    dp = [float('inf')] * (target_length + 1)
    dp[0] = 0

    for i in range(1, target_length + 1):
        for length in rocket_sections:
            if i >= length:
                dp[i] = min(dp[i], dp[i - length] + 1)



    current_length = target_length
    solution = {}

    while current_length > 0:
        section_added = False
        for length in rocket_sections:
            if current_length >= length and dp[current_length] == dp[current_length - length] + 1:
                solution[length] = solution.get(length, 0) + 1
                current_length -= length
                section_added = True
                break

        if not section_added:
            solution[1] = solution.get(1, 0) + 1
            current_length -= 1

    return solution, dp[target_length]

input_line = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
target_length = 1000

rocket_sections = list(map(int, input_line.split()))
solution, sections_count = dynamic_construct_rocket(rocket_sections, target_length)

if solution:
    for length in sorted(set(rocket_sections + [1])):
        count = solution.get(length, 0)
        print(f"{count} of length {length}")
    print(f"{sections_count} rocket sections minimum")
else:
    print("Right input?")
