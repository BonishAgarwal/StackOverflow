from stack_overflow import StackOverFlow


class Demo:
    
    def main(self):
        stack_overflow = StackOverFlow()
        
        user1 = stack_overflow.add_user(
            username="Bonish",
            email = "bonish.agarwal.99@gmail.com"
        )
        
        user2 = stack_overflow.add_user(
            username="Tanuja",
            email = "tanuja.minde@gmail.com"
        )
        
        question1 = stack_overflow.ask_question(
            title = "Question 1", 
            description = "Description for Question 1", 
            author = user1
        )
        
        question2 = stack_overflow.ask_question(
            title = "Question 2", 
            description = "Description for Question 2", 
            author = user1
        )
        
        answer1 = stack_overflow.answer_questions(
            question = question1, 
            content = "Ans 1", 
            author = user2
        )
        
        stack_overflow.add_comment(
            user1, question1, "Right!!"
        )
        
        
        

d = Demo()

d.main()
        