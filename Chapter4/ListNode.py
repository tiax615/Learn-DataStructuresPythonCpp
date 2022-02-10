class ListNode:
    def __init__(self, item=None, link=None):
        '''creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link.'''

        self.item = item # 用来存储和节点相关联的数据的实例变量
        self.link = link # 用来存储序列的下一个元素的实例变量
    
    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item
    
    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link
