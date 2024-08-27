
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

 #strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.




def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]
    
    for string in strs[1:]:
        # Shorten the prefix until it matches the start of the string
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            # If prefix is reduced to empty, return ""
            if not prefix:
                return ""
    
    return prefix
print(longest_common_prefix(["flower","flow","flight"]))