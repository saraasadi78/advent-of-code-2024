# Red-Nosed Reports

def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing


def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        candidate = levels[:i] + levels[i + 1:]
        if is_safe(candidate):
            return True
    return False


def parse_reports(text):
    reports = []
    for line in text.strip().splitlines():
        reports.append([int(x) for x in line.split()])
    return reports


def part1(reports):
    return sum(1 for r in reports if is_safe(r))


def part2(reports):
    return sum(1 for r in reports if is_safe_with_dampener(r))


if __name__ == "__main__":
    with open("input.txt") as f:
        reports = parse_reports(f.read())

    print("Part 1:", part1(reports))
    print("Part 2:", part2(reports))
