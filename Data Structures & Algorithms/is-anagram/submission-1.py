class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        my_dict_s = defaultdict(int)
        my_dict_t = defaultdict(int)

        for char in s:
            my_dict_s[char] +=1 
        for char in t:
            my_dict_t[char] +=1

        return my_dict_s == my_dict_t
        
        