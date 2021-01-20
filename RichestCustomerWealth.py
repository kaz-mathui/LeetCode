class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for account in accounts:
            print(account)
            print(sum(account))
        print(list(map(sum,accounts)))
        
        return max(list(map(sum,accounts)))