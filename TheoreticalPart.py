import random
from AVLTreeList import *
from BSTList import *


def buildRandomTree(tree, i):
    n = 1000 * pow(2, i)
    # Create insertion list
    insertList = [str(j) for j in range(n)]
    # Shuffle it
    random.shuffle(insertList)
    # Insert to tree and count rebalancing operations
    ops = 0
    for elem in insertList:
        if tree.length() == 0:
            ops += tree.insert(0, elem)
        else:
            rnd = random.randrange(0, tree.length())
            ops += tree.insert(rnd, elem)
    return ops


def insertionTest():
    print("Insertion Test:")
    t1 = AVLTreeList()
    for i in range(1, 11):
        operations = buildRandomTree(t1, i)
        print("for i =", str(i) + " :", operations)


def deletionTest():
    print("Deletion Test:")
    t2 = AVLTreeList()
    for i in range(1, 11):
        # Build random tree
        buildRandomTree(t2, i)
        # Delete randomly
        ops = 0
        for j in range(t2.length()):
            rnd = random.randrange(0, t2.length())
            ops += t2.delete(rnd)
        print("for i =", str(i) + " :", ops)


def insertionDeletionTest(n):
    tree = AVLTreeList()
    ops = 0
    while tree.length() < n / 2:
        rnd = random.randint(0, tree.length())
        tree.insert(rnd, str(rnd))
    for i in range(n // 4):
        j = random.randint(0, tree.length())
        ops += tree.insert(j, str(j))
        k = random.randint(0, tree.length() - 1)
        ops += tree.delete(k)
    return ops


def question1():
    insertionTest()
    print()
    deletionTest()
    print()
    print("Insertion-Deletion Test:")
    for i in range(1, 11):
        n = 1000 * pow(2, i)
        print("for i =", str(i) + " :", insertionDeletionTest(n))


def question3_insert_first(n):
    AVL = AVLTreeList()
    BST = BSTList()
    cnt_avl_fix = 0
    cnt_bst_fix = 0
    sum_avl_depth = 0
    sum_bst_depth = 0
    for i in range(n):
        cnt_avl_fix += AVL.insert(0, str(i))
        cnt_bst_fix += BST.insert(0, str(i))
        x = AVL.select(1)
        sum_avl_depth += AVL.getDepth(x)
        y = BST.select(1)
        sum_bst_depth += BST.getDepth(y)
    return cnt_avl_fix / n, cnt_bst_fix / n, sum_avl_depth / n, sum_bst_depth / n


def question3_insert_balanced(n):
    AVL = AVLTreeList()
    BST = BSTList()
    cnt_avl_fix = 0
    cnt_bst_fix = 0
    sum_avl_depth = 0
    sum_bst_depth = 0
    i = 1
    while AVL.length() < n:
        j = 0
        while j < pow(2, i) and AVL.length() < n:
            cnt_avl_fix += AVL.insert(j, str(j))
            cnt_bst_fix += BST.insert(j, str(j))
            x = AVL.select(j + 1)
            sum_avl_depth += AVL.getDepth(x)
            y = BST.select(j + 1)
            sum_bst_depth += BST.getDepth(y)
            j += 2
        i += 1
    return cnt_avl_fix / n, cnt_bst_fix / n, sum_avl_depth / n, sum_bst_depth / n


def question3_insert_random(n):
    AVL = AVLTreeList()
    BST = BSTList()
    cnt_avl_fix = 0
    cnt_bst_fix = 0
    sum_avl_depth = 0
    sum_bst_depth = 0
    while AVL.length() < n:
        j = random.randint(0, AVL.length())
        cnt_avl_fix += AVL.insert(j, str(j))
        cnt_bst_fix += BST.insert(j, str(j))
        x = AVL.select(j + 1)
        sum_avl_depth += AVL.getDepth(x)
        y = BST.select(j + 1)
        sum_bst_depth += BST.getDepth(y)
    return cnt_avl_fix / n, cnt_bst_fix / n, sum_avl_depth / n, sum_bst_depth / n


def question3():
    print("סדרה חשבונית")
    avl_fixes = []
    avl_depths = []
    bst_fixes = []
    bst_depths = []
    for i in range(1, 11):
        n = 1000 * i
        avl_fix, bst_fix, avl_depth, bst_depth = question3_insert_first(n)
        avl_fixes.append(avl_fix)
        bst_fixes.append(bst_fix)
        avl_depths.append(avl_depth)
        bst_depths.append(bst_depth)
    print("פעולות איזון עץ AVL")
    for num in avl_fixes:
        print(num)
    print("פעולות איזון עץ BST")
    for num in bst_fixes:
        print(num)
    print("עומק הצומת עץ AVL")
    for num in avl_depths:
        print(num)
    print("עומק הצומת עץ BST")
    for num in bst_depths:
        print(num)

    print("\nסדרה מאוזנת")
    avl_fixes = []
    avl_depths = []
    bst_fixes = []
    bst_depths = []
    for i in range(1, 11):
        n = 1000 * i
        avl_fix, bst_fix, avl_depth, bst_depth = question3_insert_balanced(n)
        avl_fixes.append(avl_fix)
        bst_fixes.append(bst_fix)
        avl_depths.append(avl_depth)
        bst_depths.append(bst_depth)
    print("פעולות איזון עץ AVL")
    for num in avl_fixes:
        print(num)
    print("פעולות איזון עץ BST")
    for num in bst_fixes:
        print(num)
    print("עומק הצומת עץ AVL")
    for num in avl_depths:
        print(num)
    print("עומק הצומת עץ BST")
    for num in bst_depths:
        print(num)

    print("\nסדרה אקראית")
    avl_fixes = []
    avl_depths = []
    bst_fixes = []
    bst_depths = []
    for i in range(1, 11):
        n = 1000 * i
        avl_fix, bst_fix, avl_depth, bst_depth = question3_insert_random(n)
        avl_fixes.append(avl_fix)
        bst_fixes.append(bst_fix)
        avl_depths.append(avl_depth)
        bst_depths.append(bst_depth)
    print("פעולות איזון עץ AVL")
    for num in avl_fixes:
        print(num)
    print("פעולות איזון עץ BST")
    for num in bst_fixes:
        print(num)
    print("עומק הצומת עץ AVL")
    for num in avl_depths:
        print(num)
    print("עומק הצומת עץ BST")
    for num in bst_depths:
        print(num)


# question1()
question3()
