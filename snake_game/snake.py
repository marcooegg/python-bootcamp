from turtle import Turtle


class Snake:
    def __init__(self, segment_size: int = 20, initial_snake_size: int = 3):
        self._segment_size = segment_size
        self._segment_qty = initial_snake_size
        self._snake_body = self._create_start_body()
        self.head = self._snake_body[0]

    def create_body_part(
        self, previous_square: Turtle = None, position: int = False
    ) -> Turtle:
        new_block = Turtle(shape="square", visible=True)
        new_block.color("white")
        new_block.penup()
        new_block.speed(1)
        if position:
            new_block.setx(position * -self._segment_size)
        if previous_square:
            new_block.setpos(self._snake_body[-1].pos())
            self._snake_body.append(new_block)
            
        return new_block

    def _create_start_body(self) -> list:
        body = []
        for x in range(self._segment_qty):
            body.append(self.create_body_part(position=x))
        self._segment_qty = len(body)
        return body

    def move(self):
        previous_block_position = self.head.pos()
        self.head.forward(self._segment_size)
        for idx, block in enumerate(self._snake_body, start=0):
            if idx == 0:
                continue
            current_pos = block.pos()
            block.goto(previous_block_position)
            previous_block_position = current_pos


    def _get_snake_heading(self):
        snake_body = self._snake_body
        snake_head = snake_body[0]
        snake_heading = snake_head.heading()
        if snake_heading in [0,180]:
            return "horizontal"
        else:
            return "vertical"


    def up(self):
        if self._get_snake_heading() != "vertical":
            self.head.setheading(90)

    def down(self):
        if self._get_snake_heading() != "vertical":
            self.head.setheading(270)

    def left(self):
        if self._get_snake_heading() != "horizontal":
            self.head.setheading(180)

    def right(self):
        if self._get_snake_heading() != "horizontal":
            self.head.setheading(0)

