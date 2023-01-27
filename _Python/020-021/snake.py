from turtle import Turtle

START_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_initial_pos()
        self.head = self.segments[0]

    def create_initial_pos(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(pos)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        pass

    def _replace_pieces(self):
        for seg in range(len(self.segments)-1, 0, -1):
            self.segments[seg].goto(self.segments[seg-1].xcor(), self.segments[seg-1].ycor())

    def move(self):
        self._replace_pieces()
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # self._replace_pieces()
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        # self._replace_pieces()
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        # self._replace_pieces()
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        # self._replace_pieces()
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_initial_pos()
        self.head = self.segments[0]


