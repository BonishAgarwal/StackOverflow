# Stack Overflow Design

### Requirements
1. Users can post questions, answer questions, and comment on questions and answers.
2. Users can vote on questions and answers.
3. Questions should have tags associated with them.
4. Users can search for questions based on keywords, tags, or user profiles.
5. The system should assign reputation score to users based on their activity and the quality of their contributions.
6. The system should handle concurrent access and ensure data consistency.


### Classes, Interfaces and Enumerations
1. User
    - username: str
    - email: str
    - reputation: int

2. Question
    - title: str
    - description: str
    - created_at: datetime
    - author: User
    - comment: Comment
    - tag: Tag

3. Answer
    - content: str
    - author: User
    - question: Question
    - comment: Comment

4. Comment
    - content: str
    - author: User

5. Tag
    - name: str

6. Vote
    - type: ENUM

7. StackOverFlow (main class)

8. StackOverFlowDemo