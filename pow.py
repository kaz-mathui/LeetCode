# class Solution:
#     def myPow(self, x: float, n: int) -> float:
        
#         def fastPow(x:float,n:int) -> float:
#             if n == 0:
#                 return 1.0
#             half = fastPow(x,n/2)
#             if n%2 == 0:
#                 return half * half
#             else:
#                 return half * half * x
            
#         if n < 0:
#             x = 1 / x
#             n = - n
#         return fastPow(x,n)
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)