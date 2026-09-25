# https://zibada.guru/gcj/ks2016b/problems/#C
#
# 1. Generate the intervals according to the given formula. Here we represent each interval as [L, R).
# 2. Flatten the intervals into points (L, 'L', index) and (R, 'R', index).
# 3. Sort the points. And for the segments formed by two consecutive points, we compute the number of intervals covering it.
# 4. At the same time of step 3, we get a map from interval index to the segments it covers along with their coverage count.
# 5. For each interval, we compute the total length of segments it covers with coverage count 1.
# 6. Finally, we find the maximum length among the lengths computed in step 5, and subtract it from the total covered length to get the result.
# 7. For the total covered length, we can compute it during step 3 as well.

from collections import defaultdict


def generate_intervals(N, L1, R1, A, B, C1, C2, M):
    intervals = [(L1, R1)]

    x, y = L1, R1
    for i in range(1, N):
        x_new = (A * x + B * y + C1) % M
        y_new = (A * y + B * x + C2) % M
        intervals.append((x_new, y_new + 1) if x_new <= y_new else
                         (y_new, x_new + 1))  # represent as [L, R)

        x, y = x_new, y_new
    return intervals


def flat_intervals(intervals):
    points = []
    for index, interval in enumerate(intervals):
        L, R = interval
        points.append((L, 'L', index))
        points.append((R, 'R', index))
    return sorted(points)


def compute_total_length(points):
    total_length = 0
    current_coverage = 0

    last_position = None
    for position, typ, interval_id in points:
        if last_position is not None and position != last_position and current_coverage > 0:
            total_length += position - last_position

        if typ == 'L':
            current_coverage += 1
        else:
            current_coverage -= 1
        last_position = position
    return total_length


def compute_interval_with_segment_coverage(points):
    """ For each interval, compute the segments it covers along with their coverage count. """
    interval_with_coverage = defaultdict(list)

    last_position = None
    active_intervals = set()
    for position, typ, interval_id in points:
        if last_position is not None and position != last_position and len(
                active_intervals) > 0:
            segment = (last_position, position)
            for active_interval_id in active_intervals:
                interval_with_coverage[active_interval_id].append(
                    (segment, len(active_intervals)))

        if typ == 'L':
            active_intervals.add(interval_id)
        else:
            active_intervals.remove(interval_id)
        last_position = position
    return interval_with_coverage


def compute_interval_with_single_coverage(interval_with_coverage):
    single_coverage_segment_length = {}

    for interval_index, segments_with_coverage in interval_with_coverage.items(
    ):
        segment_length_sum_with_single_coverage = 0
        for ((start, end), coverage) in segments_with_coverage:
            if coverage != 1:
                continue

            segment_length_sum_with_single_coverage += end - start
        single_coverage_segment_length[
            interval_index] = segment_length_sum_with_single_coverage
    return single_coverage_segment_length


def solve(N, L1, R1, A, B, C1, C2, M):
    intervals = generate_intervals(N, L1, R1, A, B, C1, C2, M)
    points = flat_intervals(intervals)
    total_length = compute_total_length(points)
    interval_with_coverage = compute_interval_with_segment_coverage(points)
    interval_with_single_coverage = compute_interval_with_single_coverage(
        interval_with_coverage)
    # print(f"intervals: {intervals}")
    # print(f"points: {points}")
    # print(f"total_length: {total_length}")
    # print(f"interval_with_coverage: {interval_with_coverage}")
    # print(f"interval_with_single_coverage: {interval_with_single_coverage}")
    return total_length - max(interval_with_single_coverage.values(),
                              default=0)


T = int(input())
for t in range(1, T + 1):
    N, L1, R1, A, B, C1, C2, M = map(int, input().split())
    result = solve(N, L1, R1, A, B, C1, C2, M)
    print(f"Case #{t}: {result}")
