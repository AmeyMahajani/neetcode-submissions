class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabets = [0]*26

        key_val = defaultdict(list)

        for word in strs:
            alphabets = [0]*26
            for letter in word:
                alphabets[ord(letter)-ord('a')] += 1
            key_val[tuple(alphabets)].append(word)

        return list(key_val.values())
        



        
        