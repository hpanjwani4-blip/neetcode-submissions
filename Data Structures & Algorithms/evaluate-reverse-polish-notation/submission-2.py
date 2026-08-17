class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for op in tokens:
            if op == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif op == "-":
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif op == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif op == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b/a)
                stack.append(result)
            else:
                stack.append(int(op))

        return stack[-1]