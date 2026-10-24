
def find_different_binary_string(nums):
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i][i] == "0":
            answer.append("1")
        else:
            answer.append("0")

    return "".join(answer)


# Example
nums = ["0011", "1110", "1011","1001"]

print(find_different_binary_string(nums))
