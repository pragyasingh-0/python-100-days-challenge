# 🚀 Day 27 of #100DaysOfPython 🐍

questions = [
    ["Who is PM of India?", "A. Modi", "B. Rahul", "C. Kejriwal", "D. None", "A"],
    ["2 + 2 = ?", "A. 3", "B. 4", "C. 5", "D. 6", "B"]
]

money = 0

for q in questions:
    print(q[0])
    print(q[1], q[2], q[3], q[4])

    ans = input("Enter your answer: ")

    if ans == q[5]:
        money += 1000
        print("Correct Answer! Money:", money)
    else:
        print("Wrong Answer! Game Over")
        break

