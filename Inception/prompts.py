from prompt_class import Questions

question_prompts = [
    "What color are apples ?\n(A) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas ?\n(A) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are strawberries ?\n(A) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_prompts)) + "")


run_test(questions)
