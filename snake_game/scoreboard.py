from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("black")
        self.hideturtle()
        self.score = 0
        self.string = f"Score: {self.score}"
        self.penup()
        self.setpos((0,280))
        self.move = False
        self.align = "center"
        self.font = ("Arial",14,"normal")
        self.pencolor("white")
        self.set_score()


    def add_point(self):
        self.score += 1
        self.set_score()

    def set_score(self):
        self.clear()
        self.write_new_score()

    def write_new_score(self):
        self.pencolor("white")
        self.string = f"Score:{self.score}"
        self.write(self.string,move=self.move,align=self.align,font=self.font)

    def game_over(self):
        self.setpos(0,0)
        self.font = 24
        self.pencolor("red")
        self.write("GAME OVER",move=self.move,align=self.align,font=self.font)