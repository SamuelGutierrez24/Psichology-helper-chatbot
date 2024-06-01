[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/lsaeWt1N)

Group members:
 - Juan Camilo Salazar Quintero (A00381085)
 - Samuel Gutierrez Dominguez (A00381035)
 - Camilo Carmona Valencia (A00381090)

# Files location:

  - You can find the report in: docs/Report.pdf
  - You can find the Bayesian network design in : docs\RedBayesianaApo3.drawio.png
  - You can find the Bayesian network implementation in: PsychologyHelper\logic\bayesianNetwork.py
  - You can find the expert system implementation in: PsychologyHelper\logic\expertSystem.py
  - You can find the chat view controller in: helper\views\chat_view.py
  - You can find the tests in: helper\tests.py
    

# Use explanation:

## Set-up (After cloning the repository):

  1. Create a virtual enviroment from the root directory, in **PowerShell** you can use these commands:
     
    - pip install virtualenv
    - virtualenv venv
    - .\venv\Scripts\activate

  5. Install libraries using:
     
    - pip install django
    - pip install pgmpy
    - pip install experta
    - pip install frozendict==2.4.2
    
## Run:

  Execute test with:
  
    - python manage.py test

  Execute app with:
  
    -  py manage.py runserver

1. Type your name so start a new chat.
2. The chat is going to ask questions, you have to type 'si' or 'no'.
3. After 19 questions the chat is going to determine the codition (Stress, Depression or Anxiety).
4. Then the chat is going to ask a few more questions to determine the cause of the condition and give a final recommendation.
5. If you type again after the recommendations, the questions will re-start.

Note: 
- You can logout at any moment and the chat will save the answers up until that moment, you can continue if you login with the same name.
- If you want to see an example of the functionality you can type 'si' in all the questions, the codition will be 'depression' and the cause will be a 'reject feeling'. You can try alternating between 'si' or 'no' to see other possible results, or you can check the test cases to see all the possibilities.
   




  


