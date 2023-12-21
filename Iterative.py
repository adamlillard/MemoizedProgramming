def construct_rocket(rocket_sections, target_length):
    sections_count = {}
    current_length = 0

    rocket_sections.sort(reverse=True)

    while current_length < target_length:
        found_section = False

        for length in rocket_sections:
            if current_length + length <= target_length:
                current_length += length
                sections_count[length] = sections_count.get(length, 0) + 1
                found_section = True
                break

        if not found_section:
            current_length += 1
            sections_count[1] = sections_count.get(1, 0) + 1

    for length in sorted(set(rocket_sections + [1])):
        count = sections_count.get(length, 0)
        print(f"{count} of length {length}")

    print(f"{sum(sections_count.values())} rocket sections minimum")

input_line = "1 7 21 37 73"
target_length = 2000

rocket_sections = list(map(int, input_line.split()))
construct_rocket(rocket_sections, target_length)
