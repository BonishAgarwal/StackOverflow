from typing import List
from commentable import Commentable
from user import User
from comment import Comment

class Question(Commentable):
    def __init__(self, title: str, description: str, author: User):
        self.title = title
        self.description = description
        self.author = author
        self.comments: List[Comment] = []
        

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_author(self):
        return self.author.get_name()
    
    def get_comments(self):
        for comment in self.comments:
            comment.get_comment()
    
    def add_comment(self, comment: Comment):
        self.comments.append(comment)
    