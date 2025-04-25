class Arrow():
    def __init__(self, pos=-1):
        self.position = pos
    
    def get_position(self):
        return self.position
    
    def arrow_up(self, length):
        if ((self.position - 1) < 0):
            self.position = length
        else:
            self.position -= 1

    def arrow_down(self, length):
        if ((self.position + 1) > length):
            self.position = 0
        else:
            self.position += 1

    def arrow_start_position(self):
        self.position = 0

    def arrow_exit(self):
        self.position = -1