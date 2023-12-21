def recursive_construct_rocket(rocket_sections, target_length, current_length=0):
    if current_length == target_length:
        return {}, 0

    if current_length > target_length:
        return None, float('inf')

    min_sections = float('inf')
    min_solution = None

    for length in rocket_sections:
        new_length = current_length + length
        sub_solution, sections_count = recursive_construct_rocket(rocket_sections, target_length, new_length)

        if sections_count + 1 < min_sections:
            min_sections = sections_count + 1
            min_solution = sub_solution.copy()
            min_solution[length] = min_solution.get(length, 0) + 1

    if 1 not in min_solution:
        min_solution[1] = 1

    return min_solution, min_sections

input_line = "1 2 3 5 7 14"
target_length = 15

rocket_sections = list(map(int, input_line.split()))
solution, sections_count = recursive_construct_rocket(rocket_sections, target_length)

if solution:
    for length in sorted(set(rocket_sections + [1])):
        count = solution.get(length, 0)
        print(f"{count} of length {length}")
    print(f"{sections_count} rocket sections minimum")
else:
    print("Recursion Fairy Did Not Work.")
