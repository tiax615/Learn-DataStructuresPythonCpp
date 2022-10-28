from TreeNode import TreeNode

class BST():
    def __init__(self) -> None:
        """create empty binary search tree
        post: empty tree created"""

        self.root = None

    # 迭代插入
    def insert(self, item):
        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        if self.root is None: # handle empty tree case
            self.root = TreeNode(item)
        else:
            # start at root
            node = self.root
            # loop to find the correct spot (break to exit)
            while True:
                if item == node.item:
                    raise ValueError("Inserting duplicate item") # 重复了
                
                if item < node.item:
                    if node.left is not None:               # item goes in left subtree
                        node = node.left                    # follow existing subtree
                    else:
                        node.left = TreeNode(item)          # empty subtree, insert here
                        break
                else:
                    if node.right is not None:              # item goes in right subtree
                        node = node.right                   # follow existing subtree
                    else:
                        node.right = TreeNode(item)         # empty subtree, insert here
                        break

    # 递归插入
    def insert_rec(self, item):
        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        self.root = self._subtreeInsert(self.root, item)

    def _subtreeInsert(self, root, item):
        if root is None:
            return TreeNode(item)                                   # inserting into empty tree
        if item == root.item:                                       # the item becomes the new tree root
            raise ValueError("Inserting duplicate item")
        
        if item < root.item:
            root.left = self._subtreeInsert(root.left, item)        # modify left subtree
        else:
            root.right = self._subtreeInsert(root.right, item)      # modify right subtree

        return root # original root is root of modified tree

    def find(self, item):
        """ Search for item in BST
            post: Returns item from BST if found, None otherwise"""

        node = self.root
        while node is not None and not (node.item == item):
            if item < node.item:
                node = node.left
            else:
                node = node.right
            
        if node is None:
            return None
        else:
            return node.item

    def delete(self, item):
        """remove item from binary search tree
        post: item is removed from the tree
        """

        self.root = self._subtreeDelete(self.root, item)

    def _subtreeDelete(self, root, item):
        if root is None:                                                # Empty tree, nothing to do
            return None
        if item < root.item:                                            # modify left
            root.left = self._subtreeDelete(root.left, item)
        elif item > root.item:                                          # modify right
            root.right = self._subtreeDelete(root.right, item)
        else:                                                           # delete root
            if root.left is None:                                       # promote right subtree
                root = root.right           
            elif root.right is None:                                    # promote left subtree
                root = root.left
            else:
                # overwrite root with max of left subtree
                root.item, root.left = self._subtreeDelMax(root.left)
        return root

    def _subtreeDelMax(self, root):
        if root.right is None:                  # root is the max
            return root.item, root.left         # return max and promote left subtree
        else:
            # max is in right subtree, recursively find and delete if
            maxVal, root.right = self._subtreeDelMax(root.right)
            return maxVal, root

    def asList(self):
        """gets item in in-order traversal order
        post: returns list of items in tree in orders"""

        items = []
        self._subtreeAddItems(self.root, items)
        return items

    def _subtreeAddItems(self, root, itemList):
        if root is not None:
            self._subtreeAddItems(root.left, itemList)
            itemList.append(root.item)
            self._subtreeAddItems(root.right, itemList)

    # 访问者模式，避免生成另一个相同大小的集合
    def visit(self, f):
