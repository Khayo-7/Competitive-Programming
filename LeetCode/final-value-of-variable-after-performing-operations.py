class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        value = 0
        for operation in operations:

            # if operation in ['++X', 'X++']:
            # if operation == '++X' or operation == 'X++':
            if '+' in operation:
                value += 1
            else:
                value -= 1
        
        return value