class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}

        for i in s:
            dict_1[i] = dict_1.get(i, 0)+1
        for j in t:
            dict_2[j] = dict_2.get(j, 0)+1

        size_1 = len(dict_1)
        size_2 = len(dict_2)
        if size_1> size_2:
            iterable_d = dict_1
            not_iterable = dict_2
        else: 
            iterable_d = dict_2
            not_iterable = dict_1

        for k in iterable_d:
            if iterable_d.get(k, 0) == not_iterable.get(k, 0):
                continue
            else:
                return False
        return True 
         