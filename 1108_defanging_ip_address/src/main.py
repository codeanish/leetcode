def hello():
    return ("Hello")

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.defangIPaddr("192.168.1.1"))