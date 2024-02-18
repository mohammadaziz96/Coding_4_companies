# Given an array A and a value K, find if there is a triplet in array whose sum is equal to the given value K. If there is such a triplet present in array, then return True else return False.

class triplet:
    def __init__(self, arr, target):
        self.arr=arr
        self.target=target
    def tripletSum(self):
        for i in range(0, len(self.arr)-2):
            for j in range(i+1, len(self.arr)-1):
                for k in range(j+1, len(self.arr)):
                    if self.arr[i]+self.arr[j]+self.arr[k]==self.target:
                        return True
        return False

t=triplet([int(i) for i in input("Enter list of numbers").split(" ")], int(input("Enter your target sum: ")))
print(t.tripletSum())
