def main():
    sequences = []

    with open('input.txt', 'r') as f:
        for line in f:
            sequence = list(map(int, line.strip('\n').split(' ')))
            sequences.append(sequence)

    valid_count = len(list(filter(CheckIfReportIsSafe, sequences)))

    print(valid_count)


def CheckIfReportIsSafe(report: list[int]) -> bool:
    length_of_report = len(report)

    sorted_report = report.copy()
    sorted_desc_report = report.copy()
    sorted_report.sort()
    sorted_desc_report.sort(reverse=True)

    if ((sorted_report[0] != report[0] or sorted_desc_report[0] != report[0])
            and (sorted_report[length_of_report-1] != report[length_of_report-1])):
        print('One Match')
        print(report)
        return True

    return False

if __name__ == '__main__':
    main()