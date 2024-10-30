import sys

def main():
    nums = read_ints()
    results, _ = problem_solver(nums[0], nums[1:])
    print_results(results)

# Recursively prints the results list in ascending order
def print_results(results):
    if len(results) == 0:
        return
    print(results[0])
    print_results(results[1:])

# Recursively solves each test case and returns the results
def problem_solver(cases, data):
    if cases == 0:
        # initial state of sums list and index
        return [], 0
    sums, index = problem_solver(cases - 1, data)
    total_ints = data[index]
    # moves index to the first integer to be squared
    index += 1
    # subslice that contains the integers used for the sum of squares
    problem = data[index : index + total_ints]
    sums.append(sum_of_squares(problem))
    # moves index to the next case's data
    index += total_ints
    return sums, index

# Recursively collects sum of squares of positive integers
def sum_of_squares(nums):
    if len(nums) == 0:
        return 0
    sum_ = sum_of_squares(nums[1:])
    if nums[0] > 0:
        sum_ += nums[0] * nums[0]
    return sum_

# Recursively reads integers from standard input
def read_ints():
    line = sys.stdin.read().strip()
    if not line:
        return []
    nums = list(map(int, line.split()))
    return nums

if __name__ == "__main__":
    main()
