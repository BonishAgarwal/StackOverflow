from user import User

class Comment:
    
    def __init__(self, content, author: User):
        self.content = content
        self.author = author
    
    def get_comment(self):
        return self.content