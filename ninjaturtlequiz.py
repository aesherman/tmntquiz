# Coding for the stage 2 project.  It is a Ninja Turtle Quiz Game!

easy_answer = ["Leonardo", "Raphael", "Michaelangelo", "Donatello", "rat", "Splinter"]
easy_content = "The blue Ninja Turtle is named __1__ . " + \
             "The red Ninja Turtle is named __2__ . " + \
             "The orange Ninja Turtle is named __3__ . " + \
             "The purple Ninja Turtle is named __4__ . " + \
             "The are led by a __5__ named __6__ . "

medium_answer = ["Michaelangelo", "Leonardo", "bow", "Raphael"]
medium_content = " __1__ uses nunchucks as his weapon of choice. " + \
             "__2__ has two long swords that he uses. " + \
             "Donatello uses a __3__ to fight crime. " + \
             "__4__ fights with sigh's, which look like hand-held pitchforks!"

hard_answer = ["Shredder", "Foot", "Rocksteady", "Bebop", "April"]
hard_content = "The Turtles main enemy is named The __1__ . " + \
             "He runs a secret organization named The __2__ Clan. " + \
             "He has two evil henchman who help him. " + \
             "One is a rhino named __3__ and the other is a boar named __4__ . " + \
             "On the other hand, the Turtles have a female reporter who helps them named __5__ O'Neil."


# This function runs the game, specifically at the level selected by the player. It also takes in the players answers, and returns correct or not.
def run_game(answer , quiz_string):
	i = 0
	while(i < len(answer)):

		blank = raw_input("What goes in blank " + str(i + 1) + " ? ")

		if(word_in_pos(blank , answer) != None and i == answer.index(blank)):

			quiz_string = quiz_string.split()

			p = quiz_string.index("__" + str(i + 1) + "__")
			word = quiz_string[p]
			word = word.replace("__" + str(i + 1) + "__" , blank)
			quiz_string[p] = word

			i += 1
			print "\nCowabunga!\n"
			quiz_string = " ".join(quiz_string)
			print quiz_string + "\n"

		else:
			print("\nNope, try again!")

	print "Nice job turtle bro! You got them all!\n"

# This compares player responses to words in the list.
def word_in_pos(word, answers):

	for pos in answers:
		if pos == word:
			return pos
	return None


# This runs the start of the game, welcoming the player and having them select their level.
def main():

	play = "yes"


	while(play == "yes"):

		print "\nWelcome to the Ninja Turtle Quiz Game!"
		print "\n1. easy" + " " * 5 + "2. medium" + " " * 5 + "3. hard"

		level = raw_input("\nType in your Difficulty Level : ")

		level_Selector(level)

		play = raw_input("Do You want to play again ? (yes/no) ")
		if(play == "no"):
			print "Thanks for playing, and stay gnarly! Turtle Power!"

# This allows the player to select their difficulty level.
def level_Selector(level):
    if(level == "easy"):
        print easy_content + "\n"
        run_game(easy_answer, easy_content)

    elif(level == "medium"):
        print medium_content + "\n"
        run_game(medium_answer, medium_content)

    elif(level == "hard"):
        print hard_content + "\n"
        run_game(hard_answer, hard_content)

    else:
        level = raw_input("\nHey! That's not an option! Please type in your Difficulty Level : ")
        level_Selector(level)


if __name__ == "__main__":
        main()
