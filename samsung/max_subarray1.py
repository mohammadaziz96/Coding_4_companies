#2. You are given an array A of N integers. Find the contiguous sub-array containing at least one number which has the maximum sum and prints its sum.

def max_sub(arr):
    max_sum=float('-inf')  # maximum negative number
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray_sum=0
            for k in range(i, j+1):
                subarray_sum=subarray_sum+arr[k]
            if subarray_sum>max_sum:
                max_sum=subarray_sum
    return max_sum
a=input("Enter numbers with single space: ").split(" ")
a=[int(i) for i in a]
print(max_sub(a))
