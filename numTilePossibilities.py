class Solution(object):
    possibleTiles = 0

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        freq = self.checkFreq(tiles)
        self.traverse(tiles, freq)
        return self.possibleTiles

    def traverse(self, s, freq):
        for key in freq:
            if freq[key] == 0:
                continue
            s += key
            freq[key] -= 1
            self.possibleTiles += 1
            self.traverse(s, freq)
            freq[key] += 1

    def checkFreq(self, tiles):
        freq = dict()
        for c in set(tiles):
            freq[c] = tiles.count(c)
        return freq


if __name__ == '__main__':
    tiles = "AAABBC"
    sol = Solution()
    print(sol.numTilePossibilities(tiles))
