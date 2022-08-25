# username - ofeklevi2
# id1      - 314939398
# name1    - Yoav Shkedy
# id2      - 209124437
# name2    - Ofek Levi


from printree import *


class AVLNode(object):
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
        """Represents nodes of type AVLNode in O(1)
        @rtype: str
        @returns: Value of the node, "None" if it is a virtual node
        """
        if self.isRealNode():
            return self.value
        return "None"

    def getLeft(self):
        """Returns the left child of a node in O(1)
        @rtype: AVLNode
        @returns: The left child of self, None if there is no left child
        """
        return self.left

    def getRight(self):
        """Returns the right child of a node in O(1)
        @rtype: AVLNode
        @returns: The right child of self, None if there is no right child
        """
        return self.right

    def getParent(self):
        """Returns the parent of a node in O(1)
        @rtype: AVLNode
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

    def getSize(self):
        """Returns the size of the node in O(1)
        @rtype: int
        @returns: Size of self
        """
        return self.size

    def setSize(self, size):
        """Sets the size of a node in O(1)
        @type size: int
        @param size: The size
        """
        self.size = size

    def setLeft(self, node):
        """Sets left child of a node in O(1)
        @type node: AVLNode
        @param node: A node
        """
        self.left = node

    def setRight(self, node):
        """Sets right child of a node in O(1)
        @type node: AVLNode
        @param node: A node
        """
        self.right = node

    def setParent(self, node):
        """Sets parent of a node in O(1)
        @type node: AVLNode
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
        return self.getHeight() != -1

    def isLeaf(self):
        """Checks if a node is a leaf of its tree in O(1)
        @rtype: bool
        @returns: True if the node is a leaf
        """
        return not self.getLeft().isRealNode() and not self.getRight().isRealNode()

    def balanceFactor(self):
        """Returns the balance factor of the node in O(1)
        @rtype: int
        @returns: Balance factor of self
        """
        return self.getLeft().getHeight() - self.getRight().getHeight()


class AVLTreeList(object):
    """A class implementing the ADT list, using an AVL tree"""

    # A virtual node declared as a class variable
    # All leaves of all trees of type AVLTreeList
    # should point to this virtual node
    virtual = AVLNode(None)
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
        @type x: AVLNode
        @param x: a node
        """
        self.minimum = x

    def setMax(self, x):
        """Sets the maximum node of the tree in O(1)
        @type x: AVLNode
        @param x: a node
        """
        self.maximum = x

    def setRoot(self, x):
        """Sets the root of the tree representing the list in O(1)
        @type x: AVLNode
        @param x: A node
        """
        self.root = x

    def getRoot(self):
        """Returns the root of the tree representing the list in O(1)
        @rtype: AVLNode
        @returns: The root, None if the list is empty
        """
        # If the list is empty return None
        if self.empty():
            return None
        # Else, return the root of the tree
        return self.root

    def getTreeRoot(self):
        """Returns the root of the tree in O(1)
        @rtype: AVLNode
        @returns: The root
        """
        return self.root

    def getMin(self):
        """Returns the node with the minimum rank in the tree in O(1)
        @rtype: AVLNode
        @returns: The node with the minimum rank in the tree
        """
        return self.minimum

    def getMax(self):
        """Returns the node with the maximum rank in the tree in O(1)
        @rtype: AVLNode
        @returns: The Node with the maximum rank in the tree
        """
        return self.maximum

    def getVirtualNode(self):
        """Returns the node with the maximum rank in the tree in O(1)
        @rtype: AVLNode
        @returns: The Node with the maximum rank in the tree
        """
        return self.virtual

    def getDepth(self, x):
        """Returns the depth of a node in O(1)
        @type x: AVLNode
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
        return not self.getTreeRoot().isRealNode()

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
        @rtype: list
        @returns: The number of rebalancing operation due to AVL rebalancing
        """
        rnk = i + 1
        ops = 0
        isMin = False
        isMax = False
        # Node of rank 1 is the minimum node
        if rnk == 1:
            isMin = True
        # Node of rank n is the maximum node
        if rnk == self.length() + 1:
            isMax = True
        # Execute insertion
        tpl = self.treeInsert(self.getTreeRoot(), rnk, val, ops, isMin, isMax)
        z = tpl[0]
        ops += tpl[1]
        self.setRoot(z)
        return ops

    def treeInsert(self, x, rnk, val, ops, isMin, isMax):
        """Inserts new node to the tree with passed value at rank i + 1 in O(log(n))
        @type x: AVLNode
        @type rnk: int
        @type val: str
        @type ops: int
        @type isMin: boolean
        @type isMax: boolean
        @param x: The root of the subtree
        @param rnk: The rank of the new inserted node
        @param val: The value of the new inserted node
        @param ops: The number of rebalancing operations
        @param isMin: Indicates if the node should be set to minimum
        @param isMax: Indicates if the node should be set to maximum
        @rtype: tuple
        @returns: (root of the subtree, number of rebalancing operations)
        """
        # We have reached a virtual node,
        # replace it with the inserted node
        if not x.isRealNode():
            z = AVLNode(val)
            z.setLeft(self.getVirtualNode())
            z.setRight(self.getVirtualNode())
            if isMin:
                self.setMin(z)
            if isMax:
                self.setMax(z)
            return z, 0

        # Go right and decrement the passed rank
        if x.getLeft().getSize() + 1 < rnk:
            tpl = self.treeInsert(x.getRight(), rnk - (x.getLeft().getSize() + 1),
                                  val, ops, isMin, isMax)
            z = tpl[0]
            x.setRight(z)
            z.setParent(x)
            ops += tpl[1]

        # Go left
        elif x.getLeft().getSize() + 1 >= rnk:
            tpl = self.treeInsert(x.getLeft(), rnk,
                                  val, ops, isMin, isMax)
            z = tpl[0]
            x.setLeft(z)
            z.setParent(x)
            ops += tpl[1]

        # Balance the subtree
        return self.balance(x, ops)

    def delete(self, i):
        """Deletes the i'th item in the list
        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @returns: The number of rebalancing operation due to AVL rebalancing
        """
        rnk = i + 1
        ops = 0
        # Execute deletion
        tpl = self.treeDelete(self.getTreeRoot(), rnk, ops)
        z = tpl[0]
        ops += tpl[1]
        # Update fields of tree
        self.setRoot(z)
        z.setParent(None)
        if self.empty():
            self.setMin(self.getVirtualNode())
            self.setMax(self.getVirtualNode())
        if self.length() == 1:
            self.setMin(self.getTreeRoot())
            self.setMax(self.getTreeRoot())
        return ops

    def treeDelete(self, x, rnk, ops):
        """Deletes the node of rank i+1 in the given subtree
        @type x: AVLNode
        @type rnk: int
        @type ops: int
        @param x: The root of the subtree
        @param rnk: The rank of the node
        @param ops: The number of rebalancing operations
        @rtype: tuple
        @returns: (root of the subtree, number of rebalancing operations)
        """
        # We reached the node we want to delete
        if rnk == x.getLeft().getSize() + 1:
            # If it does not have a left child, detach
            # from parent and return its right child
            if not x.getLeft().isRealNode():
                x.setParent(None)
                return x.getRight(), 0
            # If it does not have a right child, detach
            # from parent and return its left child
            elif not x.getRight().isRealNode():
                x.setParent(None)
                return x.getLeft(), 0
            # Else, it has two children
            # Physically delete its successor from the tree
            else:
                y = x
                x = self.successor(y)
                tpl = self.deleteMin(y.getRight(), ops)
                m = tpl[0]
                # Do not count rebalance operation for successor deletion
                ops += (tpl[1] - 1)
                x.setRight(m)
                m.setParent(x)
                z = y.getLeft()
                x.setLeft(z)
                z.setParent(x)

        # Go right and decrement the passed rank
        elif x.getLeft().getSize() + 1 < rnk:
            rnk -= (x.getLeft().getSize() + 1)
            tpl = self.treeDelete(x.getRight(), rnk, ops)
            z = tpl[0]
            # If needed, update max node
            self.updateMax(x, z)
            x.setRight(z)
            z.setParent(x)
            ops += tpl[1]

        # Go left
        elif x.getLeft().getSize() + 1 > rnk:
            tpl = self.treeDelete(x.getLeft(), rnk, ops)
            z = tpl[0]
            # If needed, updated min node
            self.updateMin(x, z)
            x.setLeft(z)
            z.setParent(x)
            ops += tpl[1]

        # Balance the subtree
        return self.balance(x, ops)

    def deleteMin(self, x, ops):
        """Removes the minimum node from the given subtree in O(log(n))
        @type x: AVLNode
        @type ops: int
        @param x: The root of the subtree
        @param ops: The number of rebalancing operations
        @rtype: tuple
        @returns: (root of the subtree, number of rebalancing operations)
        """
        # If x is a leaf, return a virtual node
        if x.isLeaf():
            x.setParent(None)
            return self.getVirtualNode(), 0
        # Else, if x has only right child return it
        elif not x.isLeaf() and not x.getLeft().isRealNode():
            return x.getRight(), 0
        # Go left recursively
        tpl = self.deleteMin(x.getLeft(), ops)
        z = tpl[0]
        ops += tpl[1]
        x.setLeft(z)
        z.setParent(x)
        # Balance the subtree
        return self.balance(x, ops)

    def updateMax(self, x, z):
        """Updates the maximum node after deletion in O(1)
        @type x: AVLNode
        @type z: AVLNode
        @param x: The root of the subtree
        @param z: Right child of the root
        """
        if not z.isRealNode():
            if x.getRight() == self.getMax():
                self.setMax(x)
        else:
            if x.getRight() == self.getMax() and z == x.getRight().getLeft():
                self.setMax(z)

    def updateMin(self, x, z):
        """Updates the minimum node after deletion in O(1)
        @type x: AVLNode
        @type z: AVLNode
        @param x: The root of the subtree
        @param z: Left child of the root
        """
        if not z.isRealNode():
            if x.getLeft() == self.getMin():
                self.setMin(x)
        else:
            if x.getLeft() == self.getMin() and z == x.getLeft().getRight():
                self.setMin(z)

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
        @type x: AVLNode
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
        # Return size of root
        return self.getTreeRoot().getSize()

    def split(self, i):
        """Splits the list at the i'th index in O(log(n))
        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list according to whom we split
        @rtype: list
        @returns: A list [left, val, right], where left is an AVLTreeList representing
        the list until index i-1, right is an AVLTreeList representing the list from
        index i+1, and val is the value at the i'th index.
        """
        # In case of splitting at the first index
        if i == 0:
            x = self.getMin()
            self.delete(i)
            return [AVLTreeList(), x.getValue(), self]
        # In case of splitting at the last index
        if i == self.length() - 1:
            x = self.getMax()
            self.delete(i)
            return [self, x.getValue(), AVLTreeList()]
        # In any other case
        rnk = i + 1
        lst = self.treeSplit(self.getTreeRoot(), rnk)
        left = lst[0]
        val = lst[1]
        right = lst[2]
        # Update minimum and maximum for left and right trees
        left.updateMinMax()
        right.updateMinMax()
        return [left, val, right]

    def treeSplit(self, x, rnk):
        """Splits the tree at the node of rank rnk in O(log(n))
        @type x: AVLNode
        @type rnk: int
        @param x: The root of the subtree
        @param rnk: The rank of the node in the tree according to whom we split
        @rtype: list
        @returns: A list [left, val, right], where left is an AVLTreeList representing
        the list until index i-1, right is an AVLTreeList representing the list from
        index i+1, and val is the value at the i'th index.
        """
        # We reached the node of rank rnk
        if rnk == x.getLeft().getSize() + 1:
            T1 = self.getTreeByRoot(x.getLeft())
            T2 = self.getTreeByRoot(x.getRight())
            # Detach x from its parent and from it children
            self.detachTwoWay(x, x.getLeft(), x.getRight())
            return [T1, x.getValue(), T2]

        # Go right and decrement the passed rank
        elif x.getLeft().getSize() + 1 < rnk:
            rnk -= (x.getLeft().getSize() + 1)
            lst = self.treeSplit(x.getRight(), rnk)
            T1 = self.getTreeByRoot(x.getLeft())
            T2 = lst[0]
            val = lst[1]
            right = lst[2]
            # Detach x from its children
            self.detachTwoWay(x, x.getLeft(), x.getRight())
            # Recursively join trees
            T1.join(x, T2, True)
            return [T1, val, right]

        # Go left
        elif x.getLeft().getSize() + 1 > rnk:
            lst = self.treeSplit(x.getLeft(), rnk)
            T1 = lst[2]
            T2 = self.getTreeByRoot(x.getRight())
            val = lst[1]
            left = lst[0]
            # Detach x from its children and update size and height
            self.detachTwoWay(x, x.getLeft(), x.getRight())
            # Recursively join trees
            T1.join(x, T2, True)
            return [left, val, T1]

    def concat(self, lst):
        """Concatenates lst to self in O(log(n)) (n == self.length() + lst length())
        @type lst: AVLTreeList
        @param lst: A list to be concatenated after self
        @rtype: int
        @returns: The absolute value of the difference between the height of the AVL trees joined
        """
        diff = abs(self.getTreeRoot().getHeight() - lst.getTreeRoot().getHeight())
        # If both lists are empty
        if self.empty() and lst.empty():
            return diff
        # If self is empty, concat lst and return
        # absolute value of height differences
        elif self.empty():
            self.setNewTree(lst)
            return diff
        # If lst is empty, return absolute
        # value of height differences
        elif lst.empty():
            return diff
        # If self is of length one, insert
        # its element to lst at first index
        elif self.length() == 1:
            # Retrieve and delete in constant time
            val = self.retrieve(0)
            self.delete(0)
            lst.insert(0, val)
            self.setNewTree(lst)
            return diff
        # If lst is of length one, insert
        # its element to self at last index
        elif lst.length() == 1:
            # Retrieve and delete in constant time
            val = lst.retrieve(0)
            lst.delete(0)
            self.insert(self.length(), val)
            return diff
        # Else, get maximum node from self and delete it
        x = self.getMax()
        self.delete(self.length() - 1)
        # Join two lists
        self.join(x, lst)
        # Return height difference
        return diff

    def join(self, x, T2, split=False):
        """Joins self, x, T2 in O(abs(height(self) - height(T2)) + 1)
        @type x: AVLNode
        @type T2: AVLTreeList
        @type split: bool
        @param x: Maximum node of T1
        @param T2: T2
        @param split: Indicates if join is executed within split
        @rtype: int
        @returns: The absolute value of the difference between the height of the AVL trees joined
        """
        # If join is executed within split,
        # handle edge cases for split
        if split:
            if self.handleSplitCases(x, T2):
                return

        # Denote height of T1 = h1
        # and height of T2 = h2
        h1 = self.getTreeRoot().getHeight()
        h2 = T2.getTreeRoot().getHeight()

        # The case where h1 <= h2
        if h1 <= h2:
            # Get T1 root and set it as the left child of x
            a = self.getTreeRoot()
            a.setParent(x)
            x.setLeft(a)
            # Join and set T1 new root
            root = self.joinRight(T2.getTreeRoot(), x, h1)
            self.setRoot(root)

        # The case where h1 > h2
        elif h1 > h2:
            # Get T2 root and set it as the right child of x
            a = T2.getTreeRoot()
            a.setParent(x)
            x.setRight(a)
            # Join and set T1 new root
            root = self.joinLeft(self.getTreeRoot(), x, h2)
            self.setRoot(root)

        # Set new max for T1
        if not T2.empty():
            self.setMax(T2.getMax())

    def joinRight(self, b, x, h):
        """Joins T1, x, T2 in O(height(T2) - height(self) + 1), where height(T1) <= height(T2)
        @type b: AVLNode
        @type x: AVLNode
        @type h: int
        @param b: Node on left spine of T2
        @param x: Maximum node of T1
        @param h: Height of T1
        @rtype: AVLNode
        @returns: The root of the updated subtree
        """
        # Find first node on the left spine of T2 with height <= h
        if b.getLeft().getHeight() + 1 <= h:
            # Denote c = b's parent
            c = b.getParent()
            # Set x as b's new parent
            b.setParent(x)
            # Set b as x's new right child
            x.setRight(b)
            if c is not None:
                # Set c as x's new parent
                x.setParent(c)
                # Set x as c's new left child
                c.setLeft(x)
            # Set size and height for x
            x.setSize(x.getLeft().getSize() + x.getRight().getSize() + 1)
            x.setHeight(max(x.getRight().getHeight(), x.getLeft().getHeight()) + 1)
            # Balance
            return self.balance(x)[0]

        # Recursively go left on the spine
        z = self.joinRight(b.getLeft(), x, h)
        b.setLeft(z)
        z.setParent(b)
        # Update sizes and heights and balance upwards the tree
        b.setSize(b.getLeft().getSize() + b.getRight().getSize() + 1)
        b.setHeight(max(b.getLeft().getHeight(), b.getRight().getHeight()) + 1)
        return self.balance(b)[0]

    def joinLeft(self, b, x, h):
        """Joins T1, x, T2 in O(height(self) - height(T2) + 1), where height(T1) > height(T2)
        @type b: AVLNode
        @type x: AVLNode
        @type h: int
        @param b: Node on right spine of T1
        @param x: Maximum node of T1
        @param h: Height of T2
        @rtype: AVLNode
        @returns: The root of the updated subtree
        """
        # Find first node on the right spine of T1 with height <= h
        if b.getRight().getHeight() + 1 <= h:
            # Denote c = b's parent
            c = b.getParent()
            # Set x as b's new parent
            b.setParent(x)
            # Set b as x's new left child
            x.setLeft(b)
            if c is not None:
                # Set c as x's new parent
                x.setParent(c)
                # Set x as c's new right child
                c.setRight(x)
            # Set size and height for x
            x.setSize(x.getLeft().getSize() + x.getRight().getSize() + 1)
            x.setHeight(max(x.getRight().getHeight(), x.getLeft().getHeight()) + 1)
            # Balance
            return self.balance(x)[0]

        # Recursively go right on the spine
        z = self.joinLeft(b.getRight(), x, h)
        b.setRight(z)
        z.setParent(b)
        # Update sizes and heights and
        # balance upwards the tree
        b.setSize(b.getLeft().getSize() + b.getRight().getSize() + 1)
        b.setHeight(max(b.getLeft().getHeight(), b.getRight().getHeight()) + 1)
        return self.balance(b)[0]

    def detachTwoWay(self, x, left, right):
        """Detaches a node from its children and its children from it in O(1)
        @type x: AVLNode
        @type left: AVLNode
        @type right: AVLNode
        @param x: The parent node
        @param left: Left child
        @param right: Right child
        """
        # Execute detachment
        x.setLeft(self.getVirtualNode())
        x.setRight(self.getVirtualNode())
        left.setParent(None)
        right.setParent(None)
        # Update size and height of x
        x.setHeight(0)
        x.setSize(1)

    def setNewTree(self, other):
        """Assigns self to a new tree in O(1)
        @type other: AVLTreeList
        @param other: The new tree
        """
        self.setRoot(other.getTreeRoot())
        self.setMin(other.getMin())
        self.setMax(other.getMax())

    def getTreeByRoot(self, x):
        """Returns the subtree which is rooted by x in O(1)
        @type x: AVLNode
        @param x: The root of the tree
        @rtype: AVLTree
        @returns: The subtree which x is rooting
        """
        tree = AVLTreeList()
        tree.setRoot(x)
        if x == self.getTreeRoot().getLeft():
            tree.setMin(self.getMin())
        if x == self.getTreeRoot().getRight():
            tree.setMax(self.getMax())
        return tree

    def handleSplitCases(self, x, T2):
        """Handles edge cases for join within split
        in O(abs(height(self) - height(T2)) + 1), where at least one of the trees is empty
        @type x: AVLNode
        @type T2: AVLTreeList
        @param x: The connecting node
        @param T2: T2
        @rtype: bool
        @returns: True if an edge case caused by split was handled
        """
        # If T1 and T2 are both empty
        if self.empty() and T2.empty():
            self.setRoot(x)
            self.setMin(x)
            self.setMax(x)
            return True
        # If T1 is empty
        elif self.empty():
            self.setNewTree(T2)
            r = self.getTreeRoot()
            self.setRoot(x)
            x.setRight(r)
            r.setParent(x)
            self.topDownBalance(x)
            return True
        # If T2 is empty
        elif T2.empty():
            r = self.getTreeRoot()
            self.setRoot(x)
            x.setLeft(r)
            r.setParent(x)
            self.topDownBalance(x)
            return True
        return False

    def topDownBalance(self, x):
        """Balances the subtree that is rooted by x
         as long as it is not balanced in O(log(n))
         @type x: AVLNode
         @param x: The root of the subtree
         """
        # Balance once to set the root
        z = self.balance(x)[0]
        self.setRoot(z)
        # Balance the subtree rooted by x
        # as long as it is not balanced
        while x.balanceFactor() > 1 or x.balanceFactor() < -1:
            self.balance(x)

    def updateMinMax(self):
        """Updates minimum and maximum nodes of a tree in O(log(n))"""
        self.setMin(self.subTreeMin(self.getTreeRoot()))
        self.setMax(self.subTreeMax(self.getTreeRoot()))

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
                return i
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

    def rotateRight(self, x):
        """Rotates the given subtree to the right in O(1)
        @type x: AVLNode
        @param x: The root of the subtree
        @rtype: AVLNode
        @returns: The root of the left rotated subtree
        """
        # Execute rotation
        y = x.getLeft()
        x.setLeft(y.getRight())
        y.getRight().setParent(x)
        if x.getParent() is not None:
            # If x is a left child
            if x.getParent().getLeft() == x:
                x.getParent().setLeft(y)
            # If x is a right child
            if x.getParent().getRight() == x:
                x.getParent().setRight(y)
        y.setParent(x.getParent())
        y.setRight(x)
        y.setSize(x.getSize())
        x.setParent(y)
        # Update sizes and heights
        x.setSize(1 + x.getLeft().getSize() + x.getRight().getSize())
        x.setHeight(1 + max(x.getLeft().getHeight(), x.getRight().getHeight()))
        y.setHeight(1 + max(y.getLeft().getHeight(), y.getRight().getHeight()))
        # Return the new root of the rotated subtree
        return y

    def rotateLeft(self, x):
        """Rotates the given subtree to the left in O(1)
        @type x: AVLNode
        @param x: The root of the subtree
        @rtype: AVLNode
        @returns: The root of the right rotated subtree
        """
        # Execute rotation
        y = x.getRight()
        x.setRight(y.getLeft())
        y.getLeft().setParent(x)
        if x.getParent() is not None:
            # If x is a left child
            if x.getParent().getLeft() == x:
                x.getParent().setLeft(y)
            # If x is a right child
            if x.getParent().getRight() == x:
                x.getParent().setRight(y)
        y.setParent(x.getParent())
        y.setLeft(x)
        y.setSize(x.getSize())
        x.setParent(y)
        # Update sizes and heights
        x.setSize(1 + x.getLeft().getSize() + x.getRight().getSize())
        x.setHeight(1 + max(x.getLeft().getHeight(), x.getRight().getHeight()))
        y.setHeight(1 + max(y.getLeft().getHeight(), y.getRight().getHeight()))
        # Return the new root of the rotated subtree
        return y

    def balance(self, x, ops=0):
        """Restores the AVL tree property of the subtree in O(1)
        @type x: AVLNode
        @type ops: int
        @param x: The root of the subtree
        @param ops: int
        @rtype: tuple
        @returns: (root of the balanced subtree, number of rebalancing operations)
        """
        # Indicates if x needs height adjustment
        heightAdj = self.needsHeightAdj(x)
        # Update x's size and height
        x.setSize(1 + x.getLeft().getSize() + x.getRight().getSize())
        x.setHeight(1 + max(x.getLeft().getHeight(), x.getRight().getHeight()))

        # BF < -1 implies left rotation is needed
        if x.balanceFactor() < -1:
            # BF of right child > 0 implies right rotation
            # of right child subtree is needed first
            if x.getRight().balanceFactor() > 0:
                # Right rotation
                x.setRight(self.rotateRight(x.getRight()))
                # Increment number of rebalancing operations
                ops += 1
            # Left rotation
            x = self.rotateLeft(x)
            # Increment number of rebalancing operations
            ops += 1

        # BF > 1 implies right rotation is needed
        elif x.balanceFactor() > 1:
            # BF of left child < 0 implies left rotation
            # of left child subtree is needed first
            if x.getLeft().balanceFactor() < 0:
                # left rotation
                x.setLeft(self.rotateLeft(x.getLeft()))
                # Increment number of rebalancing operations
                ops += 1
            # Right rotation
            x = self.rotateRight(x)
            # Increment number of rebalancing operations
            ops += 1

        # Else, no rotation needed
        else:
            # Height adjustment is considered a rebalancing
            # operation iff no rotation was executed
            if heightAdj:
                ops += 1
        return x, ops

    def needsHeightAdj(self, x):
        """Returns if the height adjustment of a node counts as a rebalancing operation in O(1)
        @type x: AVLNode
        @param x: A node
        @returns: True if the height adjustment of a node counts as a rebalancing operation
        """
        return x.getHeight() != max(x.getLeft().getHeight(), x.getRight().getHeight()) + 1

    def subTreeMin(self, x):
        """Returns the node with the minimum rank in the subtree in O(log(n))
        @type x: AVLNode
        @param x: The root of the subtree
        @rtype: AVLNode
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
        @type x: AVLNode
        @param x: The root of the subtree
        @rtype: AVLNode
        @returns: The Node with the maximum rank in the subtree
        """
        # If tree is empty return virtual node
        if self.empty():
            return self.getVirtualNode()
        # If x is a virtual node
        elif not x.isRealNode():
            return x
        # If x has no right child then x
        # has the highest rank in its subtree
        elif not x.getRight().isRealNode():
            return x
        # Else, recursively return the
        # maximum in x.right subtree
        return self.subTreeMax(x.getRight())

    def predecessor(self, x):
        """Returns the predecessor of a node in O(log(n))
        @type x: AVLNode
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
        @type x: AVLNode
        @param x: A node
        @rtype: AVLNode
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
        @rtype: AVLNode
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
        @rtype: AVLNode
        @returns: The node of rank k in the tree
        """
        x = self.subTreeSize(k)
        r = x.getLeft().getSize() + 1
        while k != r:
            if k < r:
                if x.getLeft().isRealNode():
                    x = x.getLeft()
                r = x.getLeft().getSize() + 1
            else:
                if x.getRight().isRealNode():
                    x = x.getRight()
                k -= r
                r = x.getLeft().getSize() + 1
        return x

    def rank(self, x):
        """Returns the rank of the node in O(log(n))
        @type x: AVLNode
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


tree = AVLTreeList()
tree_2 = AVLTreeList()
