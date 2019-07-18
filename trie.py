# Implementation of a Trie data structure for pattern searching

class TrieNode(object):
    """
    Our trie node
    """
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word?
        self.word_finished = False
        # how many times this character appeared?
        self.counter = 1

def add(root, word: str):
    """
    Add a word in the trie
    """
    node = root
    for char in word:
        found_in_child = False
        # search for char in the children of the present node
        for child in node.children:
            if child.char == char:
                # if we find it, increase order by 1
                child.counter += 1
                # and point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # point node to the new child
            node = new_node
    # Mark as end of word
    node.word_finished = True

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return if prefix exists and how many
    """
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # search all children in present node
        for child in node.children:
            if child.char == char:
                # we found the char
                char_not_found = False
                # assign node as the children containing the char and break
                node = child
                break
        if char_not_found:
            return False, 0
    # We have found the prefix and we are at the node that indicates
    # the count of the prefix
    return True, node.counter
