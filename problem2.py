"""
TC: O(1) for all ythe user operation, constructor O(n) to initially add numbers to q
SP: O(n) to store numbers in set and q"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.phoneDir = deque()
        for i in range(maxNumbers):
             self.phoneDir.append(i)
        self.assigned = set()
        

    def get(self) -> int:
        num = self.phoneDir.popleft() if self.phoneDir else -1
        self.assigned.add(num)
        return num
        

    def check(self, number: int) -> bool:
        return number not in self.assigned
        

    def release(self, number: int) -> None:
        if not self.check(number):
            self.assigned.remove(number)
            self.phoneDir.append(number)
            


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)