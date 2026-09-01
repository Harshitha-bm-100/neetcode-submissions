class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                num2 = my_stack.pop()
                num1 = my_stack.pop()
                if token == "+":
                    my_stack.append(num1+num2)
                elif token == "-":
                    my_stack.append(num1-num2)
                elif token == "*":
                    my_stack.append(num1*num2)
                elif token == "/":
                    my_stack.append(int(num1/num2))
            else:
                my_stack.append(int(token))

        return my_stack[0]