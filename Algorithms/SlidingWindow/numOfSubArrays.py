class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        sum = 0

        for i in range(0, k):
            sum += arr[i]

        average = sum/k
        counter = 0

        if average >= threshold:
            counter += 1
        
        for i in range(k, len(arr)):
            sum -= arr[i-k]
            sum += arr[i]

            average = sum/k

            if average >= threshold:
                counter += 1

        
        return counter

print(Solution.numOfSubarrays(1,arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))