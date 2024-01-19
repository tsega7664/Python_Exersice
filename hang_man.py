import random
stages = [''' 
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
   /|\  |
        |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
   /|   |
        |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
   /|   |
        |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
    |   |
        |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
    o   |
        |
        |
        |
        |
===========                      
   ''',''' 
    +---+
    |   |
        |
        |
        |
        |
        |
===========                      
   ''',]
word_List = ["beekeeper","camel","banana"]
chosen_word= random.choice(word_List)
end_of_game=False
lives = 8
display = []
for j in range(0,len(chosen_word)):
     display+= "_"

while not end_of_game: 
    guess = input("guess a letter:\n ").lower()
    for i in range(0,len(chosen_word)):
        k= chosen_word[i]
        if k == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -=1 
        print(stages[lives])
        if lives==0:
            end_of_game=True
            print("you lose")  
    print(display)

    if "_" not in display:
        end_of_game=True
        print("You win.")
  