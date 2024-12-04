
#input_data = extract_input_data(2024, 2, "Day2_test.txt")
with open('/Users/anks/Documents/abc.txt', 'r') as f:
    input_data = list(map(lambda line: line.rstrip().split(), f.readlines()))

print(input_data)


### Part A ###
def is_negative(num: int) -> bool:
    """ Return True if num is negative, else False """
    return num < 0


def is_safe(nums):
    """ Determines if list of integers are "safe" based on specific conditions """
    interval = [int(nums[n+1]) - int(nums[n]) for n in range(0, len(nums)-1)]
    direction = is_negative(int(nums[1]) - int(nums[0]))
    result = 1
    if False in [1 <= abs(i) <=3 for i in interval]: result = 0
    if False in [direction == is_negative(i) for i in interval]: result = 0
    return result


# Loop list of intengers and append 1 or 0 to safe_result list for each
safe_result = []
for nums in input_data:
    safe_result.append(is_safe(nums))
print("Part A answer:", sum(safe_result)) # 572


### Part B ###
def is_safe_reduced(num_list):
    """ Determines if a list of integers is "safe" after sequentially removing one element at a time """
    safe_result = []
    for index in range(len(num_list)):
        # Remove 1 item at a time
        reduced_list = [item for i, item in enumerate(num_list) if i != index]
        # Append 1 if safe or 0 if not
        safe_result.append(is_safe(reduced_list))
    # If any list of integers is safe after removing one of the numbers, then return 1
    return 1 if any(item == 1 for item in safe_result) else 0

# Loop list of integers and append 1 or 0 to safe_result_partb list for each
safe_result_partb = []
for num_list in input_data:
    safe_result_partb.append(is_safe_reduced(num_list))
print("Part B answer:", sum(safe_result_partb)) # 612