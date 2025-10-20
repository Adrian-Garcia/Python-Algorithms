"""208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/description/

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.

boolean startsWith(String prefix) Returns true if there is a previously
inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:
    Input
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    Output
        [null, null, true, false, true, null, true]

    Explanation
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // return True
        trie.search("app");     // return False
        trie.startsWith("app"); // return True
        trie.insert("app");
        trie.search("app");     // return True

Constraints:
    - 1 <= word.length, prefix.length <= 2000
    - word and prefix consist only of lowercase English letters.
    - At most 3 * 104 calls in total will be made to insert, search,
      and startsWith.

"""
from typing import Optional


class TrieNode:
    def __init__(self, letter: Optional[str] = None, endWord: bool = False):
        self.letter = letter
        self.endWord = endWord
        self.nextLetters = dict()


class Trie:
    def __getLastLetter(self, word: str) -> Optional[TrieNode]:
        if word == "":
            return True

        currDict = self.nextLetters

        for letter in word:
            if letter not in currDict:
                return None

            currLetter = currDict[letter]
            currDict = currDict[letter].nextLetters

        return currLetter

    def __init__(self):
        self.nextLetters = dict()

    def insert(self, word: str) -> None:
        if word == "":
            return

        currDict = self.nextLetters

        for letter in word:
            if letter not in currDict:
                currLetter = TrieNode(letter)
                currDict[letter] = currLetter
            else:
                currLetter = currDict[letter]

            currDict = currDict[letter].nextLetters

        currLetter.endWord = True

    def search(self, word: str) -> bool:
        lastLetter = self.__getLastLetter(word)
        return True if lastLetter and lastLetter.endWord else False

    def startsWith(self, prefix: str) -> bool:
        lastLetter = self.__getLastLetter(prefix)
        return True if lastLetter else False
