class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            for char in string:
                # Convert character to ASCII code string + comma separator
                encoded_str += str(ord(char)) + ","
            # End of word delimiter
            encoded_str += "%"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        # Split into individual encoded words
        words = s.split("%")[:-1]

        for word in words:
            string1 = ""
            if word:
                # Split the ASCII numbers in the word
                codes = word.split(",")[:-1]
                for code in codes:
                    string1 += chr(int(code))
            result.append(string1)

        return result