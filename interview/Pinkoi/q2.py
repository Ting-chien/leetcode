def TreeConstructor(strArr):
    """
    Have a function TreeConstructor(strArr) which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"] then this forms the following tree:
    
          4
         / \
        2   7
       /
      1
    Your program should, in this case, return True if it is a valid binary tree, otherwise return False. All of the integers within the tree will be unique, which means there can only be one node in the tree with a given integer ID.
    """

    pairs = []
    for s in strArr:
        s = s.strip()[1:-1]  # 去掉括號
        a, b = s.split(',')
        pairs.append((int(a), int(b)))

    parent_of = {}      # child -> parent
    children_count = {} # parent -> 子節點數量
    nodes = set()

    for child, parent in pairs:
        nodes.add(child)
        nodes.add(parent)

        # 條件1: 同一個 child 不能有兩個不同的 parent
        if child in parent_of:
            return False
        parent_of[child] = parent

        # 條件2: 每個節點最多兩個子節點
        children_count[parent] = children_count.get(parent, 0) + 1
        if children_count[parent] > 2:
            return False

    # 條件3: 恰好只能有一個根節點(沒有父節點的節點)
    roots = [n for n in nodes if n not in parent_of]
    if len(roots) != 1:
        return False

    # 條件4: 不能有環,從每個節點往上追溯必須能終止在根節點
    for n in nodes:
        visited = set()
        cur = n
        while cur in parent_of:
            if cur in visited:
                return False
            visited.add(cur)
            cur = parent_of[cur]

    return True


# 測試
print(TreeConstructor(["(1,2)", "(2,4)", "(7,2)"]))                       # True
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))     # True
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))             # False