from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=10, pady=10, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="test text", fill="black", font=("arial", 12, "italic"), width= 280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady= 20)
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.get_next_question()


        # Score UI
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, padx=20, pady=20)

        # True button UI
        self.true_button = Button(image=self.true_img, fg="white", bg=THEME_COLOR)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)
        # False button UI
        self.false_button = Button(image=self.false_img, fg="white", bg=THEME_COLOR)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)