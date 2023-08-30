class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    # Time: O(n), where n is the length of the input array of strings
    # Space: O(N), we return new array of length N, where N is the total number of characters in the input array of strings
    def encode(self, strs):
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    # Time: O(n), where n is the length of the input encoded string
    # Space: O(n), where n is the length of the input encoded string
    def decode(self, string):
        res, i = [], 0

        while i < len(string):
            j = i
            # where "#" is delimiter, keep counting length of word until we arrive at the delimiter
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            res.append(string[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
