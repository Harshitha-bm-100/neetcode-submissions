class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0]*(len(temps))
        my_stack = []

        if not temps:
            return []

        for i in range(len(temps)):
            while my_stack and temps[i] > temps[my_stack[-1]]:
                j = my_stack[-1]
                result[j] = (i-j)
                my_stack.pop()
            my_stack.append(i)
        
        return result