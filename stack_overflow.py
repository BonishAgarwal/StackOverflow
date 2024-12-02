from typing import List

from answer import Answer
from comment import Comment
from commentable import Commentable
from question import Question
from user import User


class StackOverFlow:
    
    _instance = None
    
    def __init__(self):
        if StackOverFlow._instance is None:
            StackOverFlow._instance = self
        else:
            return StackOverFlow._instance
        
        self.users: List[User] = []
        self.questions: List[Question] = []
        self.answers: List[Answer] = []
        self.comments: List[Comment] = []
        

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user
    
    def ask_question(self, title, description, author: User):
        author.ask_question(title, description)
        
    def answer_questions(self, question: Question, content: str, author: User):
        author.answer_question(content, question)

    def add_comment(self, author: User, commentable: Commentable, content: str):
        return author.comment_on(
            commentable, content
        )
    