"""
Does not work

Hello
Hero

Fer
Feel

{
    h -> {
        e -> {
            r -> {
                o -> {}
            } 
            l -> {
                l -> {
                    o -> {}
                }
            }
        }
    }
    f -> {
        e ->
            r -> {}
            e -> {
                l -> {}
            }   
    }
}

"""


class TrieNode:
    def __init__(self, char, endOfWord=False, trieNodes=dict()):
        self.char = char
        self.endOfWord = endOfWord
        self.trieNodes = trieNodes


class Trie:
    def __init__(self) -> None:
        self.words = dict()

    def insert(self, word: str) -> None:
        word = word.lower()
        currTrieNode = None
        currTrieDict = self.words

        for i in range(len(word)):
            currChar = word[i]

            print("Pre--------------------------")
            print(" i                       ", i)
            print(" currChar                ", currChar)
            print(" currTrieNode            ", currTrieNode)
            print(" currTrieDict            ", currTrieDict)

            if currChar in currTrieDict:
                currTrieNode = currTrieDict[currChar]

            else:
                newTrieNode = TrieNode(currChar)
                currTrieDict[currChar] = newTrieNode
                currTrieNode = newTrieNode

            print("Post--------------------------")
            print(" i                       ", i)
            print(" currChar                ", currChar)
            print(" currTrieDict            ", currTrieDict)
            print(" currTrieNode            ", currTrieNode)
            print(" currTrieNode.char       ", currTrieNode.char)
            print(" currTrieNode.trieNodes  ", currTrieNode.trieNodes)
            print()
            print()
            print()

            currTrieDict = currTrieNode.trieNodes

            if i == len(word) - 1:
                currTrieNode.endOfWord = True

    def search(self, word: str) -> bool:
        word = word.lower()
        currTrieNode = self.words

        for i in range(len(word)):
            currChar = word[i]
            if currChar not in currTrieNode:
                return False

            if i == len(word) - 1 and currTrieNode[currChar].endOfWord:
                return True

            currTrieNode = currTrieNode[currChar].trieNodes

        return False


trie = Trie()
trie.insert("fer")
"""
trie.insert("hello")
print(trie.search("fer"))
print(trie.search("hello"))
print(trie.search("hell"))
print(trie.search("hero"))
trie.insert("hero")
print(trie.search("hero"))
"""
