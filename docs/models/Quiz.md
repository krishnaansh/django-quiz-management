# Quizzes

Each Quiz has an nested object of there model instance ***Quiz***, ***Question***, ***Answer***  

Every time you click ```Add Quiz```, a new quiz is created along with there question and answer you can add more question as you want.

## Fields 
***questions_count*** -> it will automatically count the no of question when you create the quiz with there question and answer
***slug*** -> It will create a unique slug automatically with the quiz name (you can change by your self also)


<hr>

# Question
Each Quiz created add there instance to question model

<hr>

# Answer
Each Quiz created add there instance to question model and question model instance to answer model

## Fields
***is_correct*** -> Mark for correct answer out of 4 or you can select as need

## Answer Validation

. no duplicated choice per question

