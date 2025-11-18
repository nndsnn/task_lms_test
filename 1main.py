with open('parts.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

results = []

for i, line in enumerate(lines, 1):
    numbers = list(map(int, line.strip().split()))
    target_parity = i % 2
    total = 0
    for num in numbers:
        if abs(num) % 2 == target_parity:
            total += num
    results.append(f"Part No {i}: {total}")

with open('whole.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))
