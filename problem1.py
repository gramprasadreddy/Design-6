"""
Insert all the sentences to Trie, search for prefix, if it exists return all the words starting with that prefix and maintain a heap to return top 3 searches
TC: O(n*log k)
SP: O(n*l)* O(n*l)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.startsWith = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq):
        curr = self.root
        for i, w in enumerate(word):
            if w not in curr.children:
                curr.children[w]= TrieNode()
            curr.children[w].startsWith[word]= freq
            curr = curr.children[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            if word in curr.children[c].startsWith:
                curr.children[c].startsWith[word]+=1
            curr = curr.children[c]
        return curr.isEnd == True

    def startsWith(self, prefix: str):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return None
            curr = curr.children[c]

        return curr.startsWith


class AutocompleteEntry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        # Custom comparison logic:
        # We want to sort first by frequency in asce order,
        # then by word lexicographically in desc order.
        if self.freq == other.freq:
            return self.word > other.word  # Desc lexicographical order
        return self.freq < other.freq  # Ascending frequency order


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.dictionary = Trie()
        self.inp = ""
        for s, t in zip(sentences, times):
            self.dictionary.insert(s, t)

    def input(self, c: str) -> List[str]:
        res = []

        if c!="#":
            self.inp+=c
            sw =  self.dictionary.startsWith(self.inp)
            hq = []
            if sw:
                for k, f in sw.items():
                    entry = AutocompleteEntry(k,f)
                    heapq.heappush(hq, (entry, k))
                    if len(hq)>3:
                        heapq.heappop(hq)
                for _ in range(min(len(hq), 3)):
                    res.append(heapq.heappop(hq)[1])
        else:
            is_present = self.dictionary.search(self.inp)
            if not is_present:
                self.dictionary.insert(self.inp, 1)                
            self.inp = ""

        return res[::-1] if res else []

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)