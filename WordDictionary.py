class WordDictionary:

    def __init__(self):
        self.dic = set()

    def addWord(self, word: str) -> None:
        self.dic.add(word)
        for i in range(len(word) - 1):
            if i < len(word) - 1:
                dots = "." * (len(word) - 1 - i)
                self.dic.add(word[i] + dots)
                self.dic.add(dots + word[len(word) - i - 1:])
            # mad -> m..,ma.,mad,.ad,..d

    def search(self, word: str) -> bool:
        pass


# Your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("mad")
    param_2 = obj.search("dad")
