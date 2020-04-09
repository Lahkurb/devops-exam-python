import json
class Square():
    def __init__(self, number, square):
        self.number = number
        self.square = square

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
