def ask_question():
	question = input("What is your question?\n")
# edited by isaacyan



import random
def pick_answer():
	r=random.randint(0,19)
	answers=[
		"It is certain.",
		"It is decidedly so.",
		"Without a doubt.",
		"Yes - definitely.",
		"You may rely on it.",
		"As I see it, yes.",
		"Most likely.",
		"Outlook good.",
		"Yes.",
		"Signs point to yes.",
		"Reply hazy, try again",
		"Ask again later.",
		"Better not tell you now.",
		"Cannot predict now.",
		"Concentrate and ask again.",
		"Don't count on it.",
		"My reply is no.",
		"My sources say no.",
		"Outlook not so good.",
		"Very doubtful."
	]
	return answers[r]


# edited by wowwh
# randomly pick an answer