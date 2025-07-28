# https://leetcode.com/problems/encode-and-decode-tinyurl/description/


class Codec:
    """
    This version of Codec does not expire its URLs,
    nor does it check for previously encoded URL by hashing it.

    This one focuses on the simple mathematical aspect of the problem.
    """

    # Ideally, this would be in a database!
    links = {}
    permute = [-1]

    # Possible characters at given index (total: 62)
    chars = "0123456789"
    chars += "abcdefghijklmnopqrstuvwxyz"
    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.

        Increments the permute array as a base-62 counter and maps it to characters.
        Stores the long URL with the generated short URL.
        Eg. [0, 10, 1] -> 09a
        """
        # Increment the permute counter
        self._increment_permute()

        # Generate short URL from permute array
        short_url = "".join(self.chars[i] for i in self.permute)

        # Store the mapping
        self.links[short_url] = longUrl

        return short_url

    def _increment_permute(self) -> None:
        """Increments the permute array as a base-62 counter."""
        base = len(self.chars)

        # We start at the first digit.
        i = 0

        while i < len(self.permute):
            # Increment the current digit.
            self.permute[i] += 1

            # If we didn't overflow, we're done.
            if self.permute[i] < base:
                break

            # If we overflowed, reset the current digit to 0 and move to the next digit.
            self.permute[i] = 0
            i += 1

        # If we overflowed and reached the end of the array,
        # reset all previous digits to 0 and add a new digit.
        # This is like going from 999 to 1000 in base-10.
        if i == len(self.permute):
            self.permute = [0] * (len(self.permute) + 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.links.get(shortUrl, "")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":
    codec = Codec()

    print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
    print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))

    for number in range(100_000_000):
        print(codec.encode(number))
