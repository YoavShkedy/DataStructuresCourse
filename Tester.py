import collections
import random

from AVLTreeList import *
from BSTList import *


def check(tree):
    """Checks if the AVL tree properties are consistent

    @rtype: boolean
    @returns: True if the AVL tree properties are consistent
    """
    if tree.empty:
        return
    if not isAVL(tree):
        print("The tree is not an AVL tree!")
    if not isSizeConsistent(tree):
        print("The sizes of the tree nodes are inconsistent!")
    if not isHeightConsistent(tree):
        print("The heights of the tree nodes are inconsistent!")
    if not isRankConsistent(tree):
        print("The ranks of the tree nodes are inconsistent!")
    if not isFamilyConsistent(tree):
        print("Parent-child relations in the tree are inconsistent!")


def isAVL(tree):
    """Checks if the tree is an AVL

    @rtype: boolean
    @returns: True if the tree is an AVL tree
    """
    return isAVLRec(tree, tree.getTreeRoot())


def isAVLRec(tree, x):
    """Checks if the subtree is an AVL

    @type x: AVLNode
    @param x: The root of the subtree
    @rtype: boolean
    @returns: True if the subtree is an AVL tree
    """
    # If x is a virtual node return True
    if not x.isRealNode():
        return True
    # Check abs(balance factor) <= 1
    bf = x.balanceFactor()
    if bf > 1 or bf < -1:
        return False
    # Recursive calls
    return isAVLRec(tree, x.getLeft()) and isAVLRec(tree, x.getRight())


def isSizeConsistent(tree):
    """Checks if sizes of the nodes in the tree are consistent

    @rtype: boolean
    @returns: True if sizes of the nodes in the tree are consistent
    """
    return isSizeConsistentRec(tree, tree.getTreeRoot())


def isSizeConsistentRec(tree, x):
    """Checks if sizes of the nodes in the subtree are consistent

    @type x: AVLNode
    @param x: The root of the subtree
    @rtype: boolean
    @returns: True if sizes of the nodes in the subtree are consistent
    """
    # If x is a virtual node return True
    if not x.isRealNode():
        return True
    # Size of x should be x.left.size + x.right.size + 1
    if x.getSize() != (x.getLeft().getSize() + x.getRight().getSize() + 1):
        return False
    # Recursive calls
    return isSizeConsistentRec(tree, x.getLeft()) and isSizeConsistentRec(tree, x.getRight())


def isHeightConsistent(tree):
    """Checks if heights of the nodes in the tree are consistent

    @rtype: boolean
    @returns: True if heights of the nodes in the tree are consistent
    """
    return isHeightConsistentRec(tree, tree.getTreeRoot())


def isHeightConsistentRec(tree, x):
    """Checks if heights of the nodes in the subtree are consistent

    @type x: AVLNode
    @param x: The root of the subtree
    @rtype: boolean
    @returns: True if heights of the nodes in the subtree are consistent
    """
    # If x is a virtual node return True
    if not x.isRealNode():
        return True
    # Height of x should be maximum of children heights + 1
    if x.getHeight() != max(x.getLeft().getHeight(), x.getRight().getHeight()) + 1:
        return False
    # Recursive calls
    return isSizeConsistentRec(tree, x.getLeft()) and isSizeConsistentRec(tree, x.getRight())


def isRankConsistent(tree):
    """Checks if the ranks of the nodes in the tree are consistent

    @rtype: boolean
    @returns: True if the ranks of the nodes in the tree are consistent
    """
    root = tree.getTreeRoot()
    for i in range(1, root.getSize()):
        x = tree.select(i)
        r = tree.rank(x)
        if i != r:
            return False
    nodesList = nodes(tree)
    for node in nodesList:
        if node != tree.select(tree.rank(node)):
            return False
    return True


def nodes(tree):
    """Returns a list of the nodes in the tree sorted by index in O(n)

    @rtype: list
    @returns: A list of the nodes in the tree sorted by index
    """
    lst = []
    nodesInOrder(tree, tree.getTreeRoot(), lst)
    return lst


def nodesInOrder(tree, x, lst):
    """Adds the nodes in the subtree to the list
     following an in-order traversal in O(n)

    @type x: AVLNode
    @type lst: list
    @param x: The root of the subtree
    @param lst: The list
    """
    if not x.isRealNode():
        return
    nodesInOrder(tree, x.getLeft(), lst)
    lst.append(x)
    nodesInOrder(tree, x.getRight(), lst)


def isFamilyConsistent(tree):
    """Checks if parent-child relations are consistent in the tree

    @rtype: boolean
    @returns: True if parent-child relations are consistent in the tree
    """
    if tree.empty():
        return True
    if tree.getTreeRoot().getParent() is not None:
        return False
    return isFamilyConsistentRec(tree, tree.getTreeRoot())


def isFamilyConsistentRec(tree, x):
    """Checks if parent-child relations are consistent in the subtree

    @rtype: boolean
    @type x: AVLNode
    @param x: The root of the subtree
    @returns: True if parent-child relations are consistent in the subtree
    """
    if not x.isRealNode():
        return True
    if x.getLeft().isRealNode():
        if x.getLeft().getParent() is not x:
            return False
    if x.getRight().isRealNode():
        if x.getRight().getParent() is not x:
            return False
    if x is not tree.getTreeRoot():
        if x.getParent().getRight() is not x and x.getParent().getLeft() is not x:
            return False
    return isFamilyConsistentRec(tree, x.getLeft()) and isFamilyConsistentRec(tree, x.getRight())


def buildAlphabetTree():
    t = AVLTreeList()
    j = 0
    for i in range(97, 123):
        t.insert(j, chr(i))
        j += 1
    return t


def buildNumbersTree(start, stop):
    t = AVLTreeList()
    j = 0
    for i in range(start, stop):
        t.insert(j, str(i))
        j += 1
    return t


def copyTree(tree):
    t1 = AVLTreeList()
    nodesList = tree.nodes()
    copyTreeRec(t1, nodesList, nodesList)
    return t1


def copyTreeRec(tree, nodesList, og):
    if len(nodesList) == 1:
        tree.insert(og.index(nodesList[0]), nodesList[0].getValue())
        return
    copyTreeRec(tree, nodesList[:len(nodesList) // 2], og)
    copyTreeRec(tree, nodesList[(len(nodesList) // 2):], og)


def splitTest(tree, i):
    print("The given tree:")
    print(tree)
    lst = tree.split(i)
    left = lst[0]
    val = lst[1]
    right = lst[2]
    print("Splitting by", val + str(":"))
    print()
    print("1. Left:")
    print(left)
    if not left.empty():
        print(" a. Left minimum:", left.getMin())
        print(" b. Left root:", left.getTreeRoot())
        print(" c. Left maximum:", left.getMax())
    else:
        print(" a. Left minimum: Virtual node")
        print(" b. Left root: Virtual node")
        print(" c. Left maximum: Virtual node")
    check(left)
    print()
    print("2. Right:")
    print(right)
    if not right.empty():
        print(" a. Right minimum:", right.getMin())
        print(" b. Right root:", right.getTreeRoot())
        print(" c. Right maximum:", right.getMax())
    else:
        print(" a. Right minimum: Virtual node")
        print(" b. Right root: Virtual node")
        print(" c. Right maximum: Virtual node")
    check(right)


def rec_random_split(tree, S):
    if tree.length() == 0:
        return S
    i = random.randrange(0, tree.length())
    lst = tree.split(i)
    T1 = lst[0]
    check(T1)
    S.add(lst[1])
    T2 = lst[2]
    check(T2)
    rec_random_split(T1, S)
    rec_random_split(T2, S)
    return S


def random_split_whole_tree(tree):
    nodesSet = set(tree.listToArray())
    S = rec_random_split(tree, set())
    print("S = ", S, "\n")
    print("nodesList =", nodesSet, "\n")
    if len(S) != len(nodesSet):
        print("The tree was not split correctly :(")
        return
    if collections.Counter(nodesSet) != collections.Counter(S):
        print("The tree was not split correctly :(")
    print("The tree was split perfectly :)")
    return


# SPLIT TEST FOR EVERY NODE IN ALPHABET TREE
# for i in range(26):
#     t = buildAlphabetTree()
#     splitTest(t, i)
#     print()
#     print("/////////////////////////////////////////////////////////////////////////////////////")
#     print()


# GET EVERY NODE IN TREE BY SPLITTING
# random_split_whole_tree(buildNumbersTree(0, 1000))

tree = buildAlphabetTree()
tree.delete(10)
print(tree)
