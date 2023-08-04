from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quzzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150, 125,
            text="",
            fill=THEME_COLOR, width=280,
            font=("Arial", 20, "italic")
        )

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=self.true_btn_handler)
        self.true_button.grid(column=0, row=2)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, command=self.false_btn_handler)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You're reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_btn_handler(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_btn_handler(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        print("is right: ", is_right)
        self.canvas.config(bg="green" if is_right else "red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
