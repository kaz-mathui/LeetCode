class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: return []
        dic, height, res = {}, [], []
        for i in range(len(people)):
            p = people[i]
            if p[0] in dic:
                dic[p[0]] += (p[1], i),
            else:
                dic[p[0]] = [(p[1], i)]
                height += p[0],
        height.sort()
        # print(height)
        print(dic)
        for h in height[::-1]:
            dic[h].sort()
            for p in dic[h]:
                print(p)
                # まじで不思議
                res.insert(p[0], people[p[1]])
        return res
