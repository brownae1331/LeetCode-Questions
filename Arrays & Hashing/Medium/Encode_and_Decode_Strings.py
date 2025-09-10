"""
Question:
        Design an algorithm to encode a list of strings to a single string. 
        The encoded string is then decoded back to the original list of strings.

        Constraints:
            - 0 <= strs.length < 100
            - 0 <= strs[i].length < 200
            - strs[i] contains only UTF-8 characters
"""

def encode(strs: list[str]) -> str:
    """
    The encode function concatenates each string with its length followed by a delimiter (#),
    ensuring the decoder knows exactly how many characters to read for each string.

    Time Complexity: O(m) - where m is the sum of lengths of all the strings.
    Space Complexity: O(m + n) - where n is the number of strings.
    """
    encode_str = ""
    for s in strs:
        encode_str = encode_str + str(len(s)) + "#" + s
    return encode_str


def decode(s: str) -> list[str]:
    """
    This function reverses the process by reading characters until it finds #, interpreting the preceding digits as the lenth of the next string.
    This method guarantess correct decoding even if the original strings contain #, since length are always used to identify boundaries.

    Time Complexity: O(m)
    Space Complexity: O(m + n)
    """
    res = []
    i = 0
    while i < len(s):
        num_str = ""
        while s[i] != "#":
            num_str = num_str + s[i]
            i += 1
        start = i + 1
        end = i + 1 + int(num_str)
        res.append(s[start:end])
        i = end
    return res


if __name__ == "__main__":
    string = encode(strs=["neet", "code", "love", "you"])
    print(string)
    output = decode(string)
    print(output)