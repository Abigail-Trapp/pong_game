from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(200)
        self.computer_score = 0
        self.player_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):    
        self.write( f"{self.computer_score}" + "          " + f"{self.player_score}", align='center', font=('Arial', 50, 'normal'))

    def update_player_score(self):
        self.player_score += 1
        self.clear()
        self.update_scoreboard()
    
    def update_computer_score(self):
        self.computer_score += 1
        self.clear()
        self.update_scoreboard()