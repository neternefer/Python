from survey import AnonymousSurvey

question = "What language do you speak? "
new_survey = AnonymousSurvey(question)

new_survey.show_question()
print("Enter q at any time to quit. \n")

while True:
	response = input("Language: ")
	if response != 'q':
		new_survey.store_response(response)
	else:
		break
new_survey.show_results()
