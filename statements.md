1.) PROBLEM STATEMENT::

Studying from textbooks or notes can often be tiresome, repetitive and inefficient for many students. Students frequently struggle to organize their study materials, revise effectively, and track their progress.
Traditional flashcards require manual preparation and lack features that help students measure growth and accuracy. There is a need for a simple and  interactive tool that helps students study in a structured and engaging manner  also providing feedback on their performance.
This project addresses these issues by providing a Python-based study helper that:
.)Allows users to create digital flashcards.
.)Enables repeated practice of difficult question.
.)Offers chapter reading through the 5 step study method:Survey, Question, Read, Recite and Review.
.)Displays performance analytics using graphs.

2.) SCOPE OF THE PROJECT::

This project focuses on providing a basic yet functional study aid that works entirely through the terminal OR command line.
The functionalities included are:
.)Allowing users to create unlimited custom flashcards.
.)Letting users test themselves and mark answers as correct or incorrect.
.)Identifying questions answered incorrectly and offering retry options.
.)Displaying a bar chart to visualize accuracy using the matplotlib module.
.)Randomizing flashcard order using the random module.
.)Providing a guided reading workflow using the 5  STEP STUDY METHOD.
.)Tracking overall performance OR growth and calculating basic statistics such as accuracy averages using the statistics module.

The scope is intentionally limited to ensure simplicity and ease of use. The project does not include:
.)Database or file storage.
.)GUI interface.
.)Multi-user support.
.)Advanced analytics or ML.

3) TARGET USERS::

This project is designed for:

.) Students :: Primary Target
.)Teachers & Tutors

Educators who want to help students practice questions in an interactive format.

.) Self-learners
  Anyone studying independently who needs a structured study tool that helps with consistency and retention.

.) Individuals preparing for exams

4) HIGH LEVEL FEATURES::
.) Flashcard Creation
Users can create an unlimited number of question AND answer flashcards.
Data is stored in Python dictionaries for easy access.

.) Flashcard Practice System:
Users test themselves by viewing questions and revealing the answers.
They TELL whether they got the question correct or wrong.
Incorrect questions are collected and offered for REDO.
Flashcard order is randomized using the random module.

.) Performance Tracking:
Tracks number of correct answers.
Generates a bar graph showing correct AND incorrect answers using matplotlib.
Ability to calculate average accuracy using statistics Module.

.) Guided Reading:
The system guides users through each step:
Survey
Question
Read
Recite
Review
Allows users to take notes and record questions.

5) SIMPLE, MENU BASED CLI Interface:
  Easy-to-use text-based choices.
  No need for technical knowledge.
