class Snake():
    def __init__(self):
        self.snake_position = [200, 60]
        self.snake_body = [[200, 60], [190, 60], [180, 60], [170, 60]]

    def get_snake_body(self):
        return self.snake_body
    
    def get_snake_position(self):
        return self.snake_position