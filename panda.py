import machine, display


class Panda(object):
    def __init__(self, tft):
        self.eyes_position = "right"
        self.tft = tft

        self.draw_panda()


    # draw panda
    def draw_panda(self):
        # body
        self.tft.circle(120, 80, 15, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        self.draw_hands()
        self.draw_legs()
        # body - inner black
        self.tft.circle(120, 80, 13, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.draw_head()


    # draw panda's head
    def draw_head(self):
        # head
        self.tft.circle(120, 60, 18, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        # nose
        self.tft.circle(120, 68, 2, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        # eyes
        self.tft.circle(112, 58, 6, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.circle(114, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
        self.tft.circle(128, 58, 6, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.circle(130, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
        # ears
        self.tft.circle(104, 45, 7, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        self.tft.circle(104, 45, 5, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.circle(136, 45, 7, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        self.tft.circle(136, 45, 5, color=self.tft.BLACK, fillcolor=self.tft.BLACK)


    # draw panda's hands
    def draw_hands(self):
        self.tft.ellipse(101, 78, 8, 4, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        self.tft.ellipse(139, 78, 8, 4, color=self.tft.WHITE, fillcolor=self.tft.WHITE)


    # draw panda's hands
    def draw_legs(self):
        self.tft.ellipse(110, 95, 6, 7, color=self.tft.WHITE, fillcolor=self.tft.WHITE)
        self.tft.ellipse(130, 95, 6, 7, color=self.tft.WHITE, fillcolor=self.tft.WHITE)


    def move_eyes(self):
        self.tft.circle(112, 58, 6, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        self.tft.circle(128, 58, 6, color=self.tft.BLACK, fillcolor=self.tft.BLACK)
        if self.eyes_position == "right":
            # move eyes to the left
            self.tft.circle(110, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
            self.tft.circle(126, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
            # set eyes_position
            self.eyes_position = "left"
        else:
            # move eyes to the right
            self.tft.circle(114, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
            self.tft.circle(130, 58, 2, color=self.tft.DARKGREEN, fillcolor=self.tft.DARKGREEN)
            # set eyes_position
            self.eyes_position = "right"
