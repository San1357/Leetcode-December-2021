#Problem no : 1153
#Problem name : String Transforms Into Another String
 
#time : O(N)
#space  : O(K)

#Code:

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        conversion_mappings = dict()
        unique_characters_in_str2 = set()
        
        
        for letter1, letter2 in zip(str1, str2):
            if letter1 not in conversion_mappings:
                conversion_mappings[letter1] = letter2
                unique_characters_in_str2.add(letter2)
            elif conversion_mappings[letter1] != letter2:
                
                return False
        
        
        if len(unique_characters_in_str2) < 26:
            return True
        
        return False
