class Band:

    def __init__(self, type=""):
        self.type = type
        self.musicians = []

    def __str__(self):
        return f"{self.type} ({self.musicians}"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for i in range(1, 4, 1):
            if not self.musicians:
                return f"{self.musicians[2 * i - 2]} needs an instrument!"
            return f"{self.musicians[2 * i - 2]} is playing: {self.musicians[2 * i - 1]}"