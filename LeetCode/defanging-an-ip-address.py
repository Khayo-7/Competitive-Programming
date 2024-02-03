class Solution:
    def defangIPaddr(self, address: str) -> str:

        defanging_address = address.replace('.', '[.]')
        
        return defanging_address