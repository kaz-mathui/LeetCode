# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         hash_map = []
#         count = 0
#         for email in emails:
#             first = email[:email.find('@')+1]
#             first = first[:first.find('+')].replace('.','')
#             second = email[email.find('@')+1:]
#             print(first,second)
#             if first + '@' + second in hash_map:
#                 continue
#             else:
#                 hash_map.append(first + '@' + second)
#                 count += 1
#         return count
            
class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)