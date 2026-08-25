class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            prev = self.min_stack[-1]
            self.min_stack.append(min(prev, val))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    # Test cases format: (operations, arguments, expected_outputs)
    test_cases = [
        (
            ["MinStack","push","push","push","getMin","pop","top","getMin"],
            [[],[-2],[0],[-3],[],[],[],[]],
            [None,None,None,None,-3,None,0,-2]
        ),
        (
            ["MinStack", "push", "push", "getMin", "getMin", "push", "getMin", "getMin", "top", "getMin", "pop", "push", "push", "getMin", "push", "pop", "top", "getMin", "pop"],
            [[], [-10], [14], [], [], [-20], [], [], [], [], [], [10], [-7], [], [-7], [], [], [], []],
            [None, None, None, -10, -10, None, -20, -20, -20, -20, None, None, None, -10, None, None, -7, -10, None]
        )
    ]
    
    all_passed = True
    
    for i, (ops, args, expected) in enumerate(test_cases):
        print(f"Test case {i+1}:")
        
        try:
            obj = None
            for j in range(len(ops)):
                op = ops[j]
                arg = args[j]
                exp = expected[j]
                
                if op == "MinStack":
                    obj = MinStack()
                    res = None
                elif op == "push":
                    res = obj.push(arg[0])
                elif op == "pop":
                    res = obj.pop()
                elif op == "top":
                    res = obj.top()
                elif op == "getMin":
                    res = obj.getMin()
                
                if res == exp:
                    pass # We won't print every operation unless it fails or is the last one to save space, but let's print all to be verbose.
                    # print(f"  [+] PASS {op}({arg}) -> Expected: {exp}, Got: {res}")
                else:
                    print(f"  [-] FAIL {op}({arg}) -> Expected: {exp}, Got: {res}")
                    all_passed = False
            
            if all_passed:
                 print(f"  [+] PASS All {len(ops)} operations produced expected results.")
                 
        except NotImplementedError as e:
            print(f"  [-] ERROR: {e}")
            all_passed = False
        except Exception as e:
            print(f"  [-] ERROR: Exception thrown: {e}")
            all_passed = False
        print("-" * 30)
        
    if all_passed:
        print("\nResult: All test cases passed!")
    else:
        print("\nResult: Some test cases failed. Keep trying!")
