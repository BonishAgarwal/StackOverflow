from typing import List
from answer import Answer
from comment import Comment
from question import Question


class User:
    
    def __init__(self, name, email, reputation=0):
        self.name = name
        self.email = email
        self.reputation = reputation
        self.comments: List[Comment] = []
        self.questions: List[Question] = []
        self.answers: List[Answer] = []
    
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_reputation(self):
        return self.reputation

    def comment_on(self, commentable, content):
        comment = Comment(content, self)
        self.comments.append(comment)
        self.reputation += 6
        
        commentable.add_comment(
            comment
        )
    
    def ask_question(self, title, description):
        question = Question(title, description, self)
        self.questions.append(question)
        self.reputation += 2
    
    def answer_question(self, content: str, question: Question):
        answer = Answer(content, self, question)
        self.answers.append(answer)
        self.reputation += 4