# Checkers
 
Checkers game with competent AI to play against.

___________________________________________________________________

Implementation:

I created this checkers game using the **pygame** set of modules since they are great for creating video games. The game is basically run using a simple loop checks for whose turn it is and updates the game pieces as well as check the winning game conditions before starting over again. To get the user input I used the pixel measurements of the squares of checkers board and compared it to the mouse click position from the user. Once you have those two points of data, it is relatively easy to calculate the selection that the user is trying to make.

___________________________________________________________________

Challenges:

The main challenge for this project was the algorithm for the AI to make its moves. For this I used the minimax algorithm which essentially calculates all the possible moves that can be made and calculates them using a score based system. Then the AI picks the lowest score move and plays it. The lower the score means that particular move is the least dangerous for the AI to make. This was a completely new algorithm for me as I had not used it before but once I researched it a little bit it actually made quite a bit of sense. 

___________________________________________________________________

Takeaways:
I was able to learn quite a bit from this project such as compartmentalizing different parts of the program. It was especially interesting to create the AI for the game as there are many different ways to go about it. In the future, I would like to try different algorithms to create a stronger AI to play against.

![alt text](https://raw.githubusercontent.com/harbirj/Checkers/main/assets/checkers.png)


