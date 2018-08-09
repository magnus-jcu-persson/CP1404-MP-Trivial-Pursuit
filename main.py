def main():

    game_questions = []
    with open('./Questions', 'r') as file:

        questions = file.read().split('\n')
        for row in questions:
            game_questions.append(row.split(','))


    for question in game_questions:

        askQuestion(question)


def askQuestion(question_line):

    question = question_line[0]

    print(question)
    print("A -", question_line[1])
    print("B -", question_line[2])
    print("C -", question_line[3])

    user_answer = input("Choose your Answer - A, B, C").lower()

    if user_answer == 'a':
        print('You chose A - CORRECT')

    elif user_answer == 'b' or user_answer == 'c':
        print("You chose", user_answer.upper(), "WRONG")

    else:
        print("Invalid Choice - WRONG!")


main()