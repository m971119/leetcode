def groupAnagrams(strs):
    result = []
    uniqueStrCounts = {}
    for string in strs:
        # build anagram map
        countString = ['0'] * 26
        for char in string:
            key = ord(char) - ord("a")
            countString[key] = int(countString[key])
            countString[key] += 1
            countString[key] = str(countString[key])
        key = ",".join(countString)
        if key in uniqueStrCounts:
            # push the string into result
            result[uniqueStrCounts[key]].append(string)
        else:
            result.append([string])
            uniqueStrCounts[key] = len(result) - 1
        return result

print(groupAnagrams(["cat"]))