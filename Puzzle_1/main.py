def main():
    # Create Starting Result
    result = 0
    similarity_score = 0

    # Lists to store numbers
    first_list = []
    second_list = []

    with open('input.txt', 'r') as f:
        for line in f:
            parts_of_line = line.split('   ')
            first_list.append(int(parts_of_line[0].strip()))
            second_list.append(int(parts_of_line[1].strip()))

    first_list.sort()
    second_list.sort()

    for i in range(len(first_list)):
        result += abs(first_list[i] - second_list[i])

    for i in range(len(first_list)):
        instances_in_second_list = len(list(filter(lambda x: x == first_list[i], second_list)))
        similarity_score += first_list[i] * instances_in_second_list

    print(f'Total Distance: {result}')
    print(f'Similarity Score: {similarity_score}')


if __name__ == '__main__':
    main()