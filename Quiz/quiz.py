class Quiz():
	"""docstring for Quiz
	"""
	questions = []
	answers = []

	def __init__(self, arg):
		# generate 10 random questions with numbers from 1..10
		question_number = 0
		while question_number < 10:
			
		# add these questions into self.questions

	def take_quiz(self):
		# log start time

		# asl all of the questions
		# log if they got the questions right
		# log the end time
		# show a summary

	def ask(self, question):
		ans_tuple = (False, 0)
		# log the start time
		start_time = datetime.datetime.now()
		# capture the answer
		answer = input(question.text)
		# check the answer
		# log the end_time
		end_time = datetime.datetime.now()
		# if the answer is right, send back True
		if answer == questions.answer:
			return (True, end_time)
		# otherwise, send back False
		# send back the elapsed time, too
		
	def summary(self):
		# print how many you got right: 5/10
		trues = 0
		for x in answers:
			if x:
				trues += 1
		print("You got {}/{}".format(trues, len(questions)))
		# print the total time for the quiz: 30 minutes