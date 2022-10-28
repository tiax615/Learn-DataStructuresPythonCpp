class TreeNode(object):
  def __init__(self, data = None, left = None, right = None):
    """ creates a tree node with specified data and references to left and right children"""
    
    self.item = data
    self.left = left
    self.right = right