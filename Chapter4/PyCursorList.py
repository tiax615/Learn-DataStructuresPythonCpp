from PyListCursor import PyListCursor

class PyCursorList(list):
    def getCursor(self):
        return PyListCursor(self)

def censor(wordList, forbiddenWords):
    cursor = wordList.getCursor()
    while not cursor.done():
        if cursor.getItem() in forbiddenWords:
            cursor.deleteItem()
        else:
            cursor.advance()