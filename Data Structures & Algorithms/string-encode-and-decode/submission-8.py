class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for st in strs:
            encoded_str = encoded_str + str(len(st)) + '#' + st
        
        print(encoded_str)
        return(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move past '#'
            i = j + 1

            # Extract exactly 'length' characters
            decoded.append(s[i:i + length])

            # Move to the next encoded string
            i = i + length
        return decoded