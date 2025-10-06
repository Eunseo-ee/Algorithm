from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        combos = []
        for order in orders:
            order = ''.join(sorted(order))
            combos += combinations(order, c)

        counter = Counter(combos)
        if len(counter) == 0:
            continue

        max_count = max(counter.values())
        if max_count < 2:
            continue

        for combo, cnt in counter.items():
            if cnt == max_count:
                answer.append(''.join(combo))

    return sorted(answer)