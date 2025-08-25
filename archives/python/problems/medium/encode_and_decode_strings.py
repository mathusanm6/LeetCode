from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_list = []
        for s in strs:
            encoded_list.append(str(len(s)) + "#")
            encoded_list.append(s)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        len_to_read = None
        prev = 0
        i = 1
        while i < len(s):
            if not len_to_read:
                if s[i] == "#":
                    len_to_read = int(s[prev:i])
                    if len_to_read == 0:
                        res.append("")
                        prev = i + 1
                i += 1
            else:
                res.append(s[i : i + len_to_read])
                prev = i + len_to_read
                i = i + len_to_read + 1
                len_to_read = None
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
