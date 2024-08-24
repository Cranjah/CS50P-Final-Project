### BRAINJOGGING 10/30
### Video Demo:  https://youtu.be/beAnOuwHVKo?si=xuMmsgJK94PHVJB4

### Description:

Inspired by the task "My Little Professor" of CS50P and Nintendo's casual video game "Dr. Kawashima's Brain Training", I created a terminal program, which I call "Brainjogging 10/30". For submission to CS50P and for now the terminal program written in Python3 contains three minigames and for each minigame two versions in length - what's the reason for it's naming numbers 10/30.

The first length version for each minigame is ten tasks per game, the second length version is thirty tasks per game. You can start them by writing the game's name as sys.argv[1] - so as the second command line argument. The names of the games are "--math10", "--math30", "--rps10", "--rps30", "--sentences10" and "--sentences30". So let me further explain the minigames:

In Math10 and Math30 you have to solve easy mathematical tasks, at the moment addition, subtraction, multiplication and division type of math problems is supported by the game. You can score by solving the mathematical tasks. To win the game you need to score 70% in total, just like in CS50P's problem sets - this is something all the minigames have in common.

In RPS10 and RPS30 you have to solve a given problem regarding a party of the world-famous game "Rock, Paper, Scissors". The tasks dictate whether to win or to lose on a given pose of rock, paper or scissors, you then have to choose which own pose you would like to bring into the round by typing it in. It's not as easy as it sounds, especially when you try to play it fast.

In Sentence10 and Sentence30 you have to build sentences containing five words, with each word beginning with a given and randomly chosen letter of the alphabet. This can be tricky, as quite often you get for example letters like "x" or "y" for which my personal vocabulary does not contain enough English words to build a sentence out of, which also makes sense. Unfortunately the program does not check for you, whether the sentence you created makes sense, so this is still a handicap - but as I have been a total beginner in coding, when I first started CS50P, it's somewhat okay for me and my personal usage of the terminal program.

I tried to find a architecture and design in my code, to easily implement further minigames in the future into my program via functions and make it as readable as possible. As the program as it is at the moment, depends much on random choices via Python's built-in random library, I was not properly able to implement a pytest file. In the file "test_project.py" I only test via a code snippet I found on StackOverflow if the random module works properly.

All in all CS50P has been the most challenging online course I made so far, I found it inspiring and ideal for personal growth and often enough when I solved a problem set, I was very proud of it. The tasks and everyday problems I faced in the course made me conscious about where in the world already has been a programmer to solve a specific task userfriendly for us and maybe spent days and nights with debugging his or her code. I now feel deep respect for every programmer and administrator, who contributes with his skills to our digital world we live in.
