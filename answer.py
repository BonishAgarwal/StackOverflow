from typing import List
from comment import Comment
from question import Question
from user import User


class Answer:
    def __init__(self, content: str, author: User, question: Question):
        self.content = content
        self.author = author
        self.question = question
        self.comments: List[Comment] = []
    
    def add_comment(self, comment: Comment):
        self.comments.append(comment)
    
    def get_comments(self):
        for comment in self.comments:
            comment.get_comment()