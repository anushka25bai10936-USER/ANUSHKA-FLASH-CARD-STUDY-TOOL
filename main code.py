import random
import statistics
import matplotlib.pyplot as plt



def show_progress_graph(right, total):
    """Displays a bar graph showing correct vs incorrect answers."""
    plt.figure(figsize=(6,4))
    plt.title("Flashcard Accuracy")
    plt.bar(["Correct", "Incorrect"], [right, total-right])
    plt.ylabel("Number of Questions")
    plt.show()



def flash_card_set_up():
  """ this function will be gathering the users input needed to have flash cards the user needs to study."""
  print("we will first need to set up your flash cards.")
  print("please take some time to fill in all your questions and answers.")
  print("writing down what you study is a good study tool")
  flash_card_dict={}
  begin="start"
  while begin:
    questions=input("Enter a flash card question or press enter to finish.")
    if questions == '':
      break
    answers=input("Enter the answer to that question.")
    flash_card_dict[questions]=answers

  print("Thank you for taking the time to do that , now you can study your flash cards ")
  return flash_card_dict 

def using_flash_cards(dictionary):
  """ this will go through flash cards randomly, take user input and have the user determine whether they got it correct or not.
  It will keep track of the fact whether the user got it correct or not and will keep user informed"""
  flash_cards = dictionary 
  length=len(flash_cards)
  redo_cards={}
  """new dict for the questions that user got wrong"""
  
  right=0
  for i in flash_cards:
    print(i)
    """prints question"""
    input("")
    print(flash_cards[i])
    correct=input("did you get it correct:y or n\n")
    if correct=='y':
      print("good job!")
      right+=1

    else:
      redo_cards[i]=flash_cards[i]

    if redo_cards:
      redo=input("would you like to redo the ones that you got wrong:y or n")
      if redo=='y':
        for i in redo_cards:
          print(i)
          input("")
          correct=input("did you get it correct? y or n")
          if correct == 'y':
            right+=1

    if right==length:

      print("you got all",right,"questions right.AMAZING JOB!")

    elif right==0:
     print("you need to study more ")
     again=input("would you like to do flash cards again:y or n")
     if again == 'y':
       using_flash_cards(flash_cards)

    else:
      
      print("You got",right,"out of",length,"questions right")
      again=input("would u like to do flash cards again, y or n \n")
      if again == 'y':
        using_flash_cards(flash_cards)

  
  show_progress_graph(right, length)
  

def step_method():
  print("There are 5 steps to this study help.\n"
        "This will help u study a chapter or\n"
        "this 5 steps are : survey,question,read,recite and review\n"
        "this programme will guide you through each step")
  notes =[]
  begin= 'continue'
  print("\n step 1: survey\n" 
      "\n begin by skimming through the chapter that you are studying\n"
      "\n take notes here on any headings, subheadings , images or other things that stand out to you")
  while begin:
   note = input("type your notes here or press enter to exit. press enter after each note\n") 
   
   if note=='':
     break
   notes.append(note)
  print("great job! step 2: question\n next you will wrute down all the question that you have")
  questions = []
  question = 'begin'
  while question != '':
   question = input("type your question here or press enter to exit. Press enter after each question\n")
   questions.append(question)
  print("step 3: read\n"
      "now read the chapter and look for answer to the question you just provided")
  print("here is a reminder for the question that you had")
  count = 'continue'
  while count != '':
    for i in questions: 
      print (i)
    count = input("presss enter when you are done reading and are ready to contninue to step 4")
  print("\n awesome! step 4: recite\n"
      "you will now need to summarize what you just read and answer to your question from 2")
  input("you are welcome to type it here or press enter to continue\n")
  print("\nstep5 : revision\n"
     "here are your question again you can type the answer that you found")
  for i in questions:
   print (i)
   input("type answer here: \n")

  print("here are your notes just that you can review")
  for i in notes:
   print(i)

def main():
  while True:
    choice = input("would you like to do flash cards or read a chapter? Type 'read' or 'flash' or press enter to exit the program\n")
    if choice == '':
      break
    elif choice == 'read':
      step_method()
    else:
      flash_cards= flash_card_set_up()
      using_flash_cards(flash_cards)
    print("good job studying! see you next time") 
main()



    


    
        
    
    
