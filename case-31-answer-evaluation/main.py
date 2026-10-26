# Case Study 31: String-Based Examination Answer Evaluation
key = input("Enter answer key (one character per question, e.g. ABCD): ").replace(" ", "").upper()
answers = input("Enter student answers in the same format (use - for blank): ").replace(" ", "").upper()

if len(key) == 0 or len(key) != len(answers):
    print("Answer key and student answers must have equal non-zero length.")
else:
    correct = 0
    incorrect = 0
    unanswered = 0
    negative_mark = 0.25
    score = 0
    for i in range(len(key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == key[i]:
            correct += 1
            score += 1
        else:
            incorrect += 1
            score -= negative_mark
    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print(f"Final score: {score:.2f} / {len(key)}")