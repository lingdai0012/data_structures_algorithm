# python3


class HashTable:
    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern
        self.__multiplier = 1
        self.__prime = 100000004987
        self.hashed_pattern = self.__hash_func(pattern)

    def __hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self.__multiplier + ord(c)) % self.__prime
        return ans

    def precompute(self):
        pattern_len = len(self.pattern)
        exponential_multiplier = self.__multiplier**pattern_len
        hash_table = [0] * (len(self.text) - len(self.pattern) + 1)
        hash_table[-1] = self.__hash_func(
            self.text[len(self.text) - len(self.pattern) :]
        )
        for i in range(len(self.text) - len(self.pattern) - 1, -1, -1):
            hash_table[i] = (
                self.__multiplier * hash_table[i + 1]
                + ord(self.text[i])
                - (exponential_multiplier % self.__prime)
                * ord(self.text[i + pattern_len])
            ) % self.__prime
        return hash_table


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(" ".join(map(str, output)))


def get_occurrences(pattern, text):
    hashed = HashTable(pattern, text)
    hash_table = hashed.precompute()
    hashed_pattern = hashed.hashed_pattern
    results = []
    for i in range(len(text) - len(pattern) + 1):
        if hash_table[i] == hashed_pattern:
            if text[i : i + len(pattern)] == pattern:
                results.append(i)
    return results


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
