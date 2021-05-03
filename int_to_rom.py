class Solution:
    def intToRoman(self, num: int) -> str:
        uno =["", "M", "MM", "MMM"]
        dos=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tres=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        quatro=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return uno[num//1000]+dos[(num%1000)//100]+tres[(num%100)//10]+quatro[(num%10)]