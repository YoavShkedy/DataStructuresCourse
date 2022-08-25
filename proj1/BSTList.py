from printree import *


class BSTNode(object):
    """A class representing a node in an AVL tree"""

    def __init__(self, value):
        """Constructor, you are allowed to add more fields.
        Initializes an AVL node in O(1)

        @type value: str
        @param value: Data of your node
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.size = 1

    def __repr__(self):
        """Represents nodes of type BSTNode in O(1)

        @rtype: str
        @returns: Value of the node, "None" if it is a virtual node
        """
        if self.isRealNode():
            return self.value
        return "None"

    def getLeft(self):
        """Returns the left child of a node in O(1)

        @rtype: BSTNode
        @returns: The left child of self, None if there is no left child
        """
        return self.left

    def getRight(self):
        """Returns the right child of a node in O(1)

        @rtype: BSTNode
        @returns: The right child of self, None if there is no right child
        """
        return self.right

    def getParent(self):
        """Returns the parent of a node in O(1)

        @rtype: BSTNode
        @returns: The parent of self, None if there is no parent
        """
        return self.parent

    def getValue(self):
        """Returns the value of a node in O(1)

        @rtype: str
        @returns: The value of self, None if the node is virtual
        """
        return self.value

    def getHeight(self):
        """Returns the height of a node in O(1)

        @rtype: int
        @returns: The height of self, -1 if the node is virtual
        """
        return self.height

    def setSize(self, size):
        """Sets the size of a node in O(1)

        @type size: int
        @param size: The size
        """
        self.size = size

    def setLeft(self, node):
        """Sets left child of a node in O(1)

        @type node: BSTNode
        @param node: A node
        """
        self.left = node

    def setRight(self, node):
        """Sets right child of a node in O(1)

        @type node: BSTNode
        @param node: A node
        """
        self.right = node

    def setParent(self, node):
        """Sets parent of a node in O(1)

        @type node: BSTNode
        @param node: A node
        """
        self.parent = node

    def setValue(self, value):
        """Sets value of a node in O(1)

        @type value: str
        @param value: Data
        """
        self.value = value

    def setHeight(self, h):
        """Sets the height of the node in O(1)

        @type h: int
        @param h: The height
        """
        self.height = h

    def isRealNode(self):
        """Checks if self is not a virtual node in O(1)

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        # A virtual node is of height -1
        return self.height != -1

    def isLeaf(self):
        """Checks if a node is a leaf of its tree in O(1)

        @rtype: bool
        @returns: True if the node is a leaf
        """
        return not self.getLeft().isRealNode() and not self.getRight().isRealNode()

    def getSize(self):
        """Returns the size of the node in O(1)

        @rtype: int
        @returns: Size of self
        """
        return self.size


class BSTList(object):
    """A class implementing the ADT list, using a BST"""

    # A virtual node declared as a class variable
    # All leaves of all trees of type AVLTreeList
    # should point to this virtual node
    virtual = BSTNode(None)
    virtual.setSize(0)
    virtual.setHeight(-1)

    def __init__(self):
        """ Constructor, you are allowed to add more fields.
        Initializes an empty list in O(1)

        """
        self.root = self.virtual
        self.minimum = self.virtual
        self.maximum = self.virtual

    def __repr__(self):
        """Representation of the tree

        @returns: Prints tree to console using printree
        function from Extended Introduction to CS course
        """
        out = ""
        for row in printree(self):
            out = out + row + "\n"
        return out

    def setMin(self, x):
        """Sets the minimum node of the tree in O(1)

        @type x: BSTNode
        @param x: a node
        """
        self.minimum = x

    def setMax(self, x):
        """Sets the maximum node of the tree in O(1)

        @type x: BSTNode
        @param x: a node
        """
        self.maximum = x

    def setRoot(self, x):
        """Sets the root of the tree representing the list in O(1)

        @type x: BSTNode
        @param x: A node
        """
        self.root = x

    def getRoot(self):
        """Returns the root of the tree representing the list in O(1)

        @rtype: BSTNode
        @returns: The root, None if the list is empty
        """
        # If the list is empty return None
        if self.empty():
            return None
        # Else, return the root of the tree
        return self.root

    def getTreeRoot(self):
        """Returns the root of the tree in O(1)

        @rtype: BSTNode
        @returns: The root
        """
        return self.root

    def getMin(self):
        """Returns the node with the minimum rank in the tree in O(1)

        @rtype: BSTNode
        @returns: The node with the minimum rank in the tree
        """
        return self.minimum

    def getMax(self):
        """Returns the node with the maximum rank in the tree in O(1)

        @rtype: BSTNode
        @returns: The Node with the maximum rank in the tree
        """
        return self.maximum

    def getVirtualNode(self):
        """Returns the node with the maximum rank in the tree in O(1)

        @rtype: BSTNode
        @returns: The Node with the maximum rank in the tree
        """
        return self.virtual

    def getDepth(self, x):
        """Returns the depth of a node in O(1)

        @type x: BSTNode
        @param x: A node
        @rtype: int
        @returns: The depth of node x
        """
        return abs(self.getTreeRoot().getHeight() - x.getHeight())

    def empty(self):
        """Checks if the list is empty in O(1)

        @rtype: bool
        @returns: True if the list is empty, False otherwise
        """
        return not self.root.isRealNode()

    def retrieve(self, i):
        """Retrieves the value of the i'th item in the list in O(log(i))

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: Index in the list
        @rtype: str
        @returns: The value of the i'th item in the list
        """
        # If i is first or last index,
        # return the value in constant time
        if i == 0:
            return self.getMin().getValue()
        elif i == self.length() - 1:
            return self.getMax().getValue()
        # Else, return the value of the i'th item
        node = self.select(i + 1)
        return node.getValue()

    def insert(self, i, val):
        """Inserts val at position i in the list in O(log(n))

        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: The value we inserts
        @rtype: int
        @returns: Number of rebalancing operations
        """
        z = BSTNode(val)
        z.setLeft(self.getVirtualNode())
        z.setRight(self.getVirtualNode())
        # If tree is empty
        if self.empty():
            self.setRoot(z)
            self.setMin(z)
            self.setMax(z)
            return 0
        # If tree is not empty
        else:
            # Insert-first
            if i == 0:
                x = self.getMin()
                x.setLeft(z)
                z.setParent(x)
                self.setMin(z)
            # Insert-last
            elif i == self.length():
                x = self.select(self.length())
                x.setRight(z)
                z.setParent(x)
                self.setMax(z)
            # Insertion in the middle
            elif i < self.length():
                parentNode = self.select(i)
                if not parentNode.getLeft().isRealNode():
                    parentNode.setLeft(z)
                    z.setParent(parentNode)
                else:
                    predecessor = self.predecessor(parentNode)
                    predecessor.setRight(z)
                    z.setParent(predecessor)
        # Update sizes and heights upwards the tree and set new root
        y = z
        cnt = 0
        while y.getParent() is not None:
            y = y.getParent()
            y.setSize(y.getLeft().getSize() + y.getRight().getSize() + 1)
            y.setHeight(max(y.getLeft().getHeight(), y.getRight().getHeight()) + 1)
            cnt += 1
        self.setRoot(y)
        return cnt

    def first(self):
        """Returns the value of the first item in the list in O(1)

        @rtype: str
        @returns: The value of the first item, None if the list is empty
        """
        # Return None is the list is empty
        if self.empty():
            return None
        # Else return the value of min node of tree
        minNode = self.getMin()
        return minNode.getValue()

    def last(self):
        """Returns the value of the last item in the list in O(1)

        @rtype: str
        @returns: The value of the last item, None if the list is empty
        """
        # Return None is the list is empty
        if self.empty():
            return None
        # Else return the value of max node of tree
        maxNode = self.getMax()
        return maxNode.getValue()

    def listToArray(self):
        """Returns an array representing list in O(n)

        @rtype: list
        @returns: A list of strings representing the data structure
        """
        lst = []
        self.valuesInOrder(self.getTreeRoot(), lst)
        return lst

    def valuesInOrder(self, x, lst):
        """Adds the values in the subtree to the list
         following an in-order traversal in O(n)

        @type x: BSTNode
        @type lst: list
        @param x: The root of the subtree
        @param lst: The list
        """
        if not x.isRealNode():
            return
        self.valuesInOrder(x.getLeft(), lst)
        lst.append(x.getValue())
        self.valuesInOrder(x.getRight(), lst)

    def length(self):
        """Returns the size of the list in O(1)

        @rtype: int
        @returns: The size of the list
        """
        # If the list is empty its size is 0
        if self.empty():
            return 0
        # Else, return size of root
        return self.getTreeRoot().getSize()

    def search(self, val):
        """Searches for a *value* in the list in O(n)
        @type val: str
        @param val: A value to be searched
        @rtype: int
        @returns: The first index that contains val, -1 if not found.
        """
        nodes = self.nodes()
        i = 0
        # Search for value and return
        # the first index that contains it
        for node in nodes:
            if node.getValue() == val:
                return nodes[i]
            i += 1
        # Value was not found
        return -1

    def nodes(self):
        """Returns a list of the nodes in the tree sorted by index in O(n)

        @rtype: list
        @returns: A list of the nodes in the tree sorted by index
        """
        lst = []
        self.nodesInOrder(self.getTreeRoot(), lst)
        return lst

    def nodesInOrder(self, x, lst):
        """Adds the nodes in the subtree to the list
         following an in-order traversal in O(n)

        @type x: AVLNode
        @type lst: list
        @param x: The root of the subtree
        @param lst: The list
        """
        if not x.isRealNode():
            return
        self.nodesInOrder(x.getLeft(), lst)
        lst.append(x)
        self.nodesInOrder(x.getRight(), lst)

    def subTreeMin(self, x):
        """Returns the node with the minimum rank in the subtree in O(log(n))

        @type x: BSTNode
        @param x: The root of the subtree
        @rtype: BSTNode
        @returns: Node with minimum rank in subtree
        """
        # If tree is empty, return virtual node
        if self.empty():
            return self.getVirtualNode()
        # If x is a virtual node
        elif not x.isRealNode():
            return x
        # If x has no left child then x
        # has the highest rank in its subtree
        if not x.getLeft().isRealNode():
            return x
        # Else, recursively return the
        # minimum in x.left subtree
        return self.subTreeMin(x.getLeft())

    def subTreeMax(self, x):
        """Returns the node with the maximum rank in the subtree in O(log(n))

        @type x: BSTNode
        @param x: The root of the subtree
        @rtype: BSTNode
        @returns: The Node with the maximum rank in the subtree
        """
        # If tree is empty return None
        if self.empty():
            return None
        # If self has no right child then self
        # has the highest rank in its subtree
        if not x.getRight().isRealNode():
            return x
        # Else, recursively return the
        # maximum in self.right subtree
        return self.subTreeMax(x.getRight())

    def predecessor(self, x):
        """Returns the predecessor of a node in O(log(n))

        @type x: BSTNode
        @param x: A node
        @returns: The predecessor of the node
        """
        # If x has left child, go left
        # once then all the way right
        if x.getLeft().isRealNode():
            return self.subTreeMax(x.getLeft())
        # Else, go up from x until the first turn left
        y = x.getParent()
        while y is not None and x == y.getLeft():
            x = y
            y = x.getParent()
        return y

    def successor(self, x):
        """Returns the successor of a node in O(log(n))

        @type x: BSTNode
        @param x: A node
        @rtype: BSTNode
        @return: The successor of the node
        """
        # If x has right child, go right
        # once then all the way left
        if x.getRight().isRealNode():
            return self.subTreeMin(x.getRight())
        # Else, go up from x until the first turn right
        y = x.getParent()
        while y is not None and x == y.getRight():
            x = y
            y = x.getParent()
        return x

    def subTreeSize(self, k):
        """Returns the first node whose size is greater or equals to k in O(log(k)).
        Helps execute Select in O(log(k))

        @type k: int
        @param k: Size of node
        @rtype: BSTNode
        @returns: The first node of size >= k
        """
        # Start at the minimum
        x = self.getMin()
        # Search for the first node of size >= k
        y = x.getParent()
        while y is not None:
            if y.getSize() >= k:
                return y
            x = y
            y = x.getParent()
        return x

    def select(self, k):
        """Returns the node of rank k in the tree in O(log(k))

        @type k: int
        @param k: Size of node
        @rtype: BSTNode
        @returns: The node of rank k in the tree
        """
        x = self.subTreeSize(k)
        r = x.getLeft().getSize() + 1
        while k != r:
            if k < r:
                # Search in left subtree
                if x.getLeft().isRealNode():
                    x = x.getLeft()
                r = x.getLeft().getSize() + 1
            else:
                # Search in right subtree
                if x.getRight().isRealNode():
                    x = x.getRight()
                k -= r
                r = x.getLeft().getSize() + 1
        return x

    def rank(self, x):
        """Returns the rank of the node in O(log(n))

        @type x: BSTNode
        @param x: A node
        @returns: The the rank of the node
        """
        r = x.getLeft().getSize() + 1
        y = x
        while y.getParent() is not None:
            # If y is a right child
            # consider the size of y's parent's subtree
            if y == y.getParent().getRight():
                r += (y.getParent().getLeft().getSize() + 1)
            y = y.getParent()
        return r

