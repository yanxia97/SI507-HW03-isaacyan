def ask_question():
	question = input("What is your question?\n")
	return question
# edited by isaacyan


if __name__ == "__main__":
	while True:
		question = ask_question()
		if question == "exit":
			break
		if question[-1]!='?':
			print("I’m sorry, I can only answer questions")
		else:
			break
# edited by isaacyan