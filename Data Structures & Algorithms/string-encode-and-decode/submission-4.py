class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "None"
        encoded_string = "_//".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        decoded_strings = s.split("_//")
        return decoded_strings