class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.score = 0

    def move(self, direction: str) -> int:
        dx, dy = self.directions[direction]
        new_head = (self.snake[0][0] + dx, self.snake[0][1] + dy)

        # Check if the new head is out of bounds
        if (
            new_head[0] < 0
            or new_head[0] >= self.height
            or new_head[1] < 0
            or new_head[1] >= self.width
        ):
            return -1

        # Check if the snake collides with itself
        if new_head in self.snake and new_head != self.snake[-1]:
            return -1

        # Check if there's food at the new head position
        if self.food and list(self.food[0]) == list(new_head):
            self.food.popleft()
            self.score += 1
        else:
            self.snake.pop()

        self.snake.appendleft(new_head)
        return self.score
