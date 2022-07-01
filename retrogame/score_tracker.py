import json
from retrogame.constants import FILE_PATH


class Score:
    def __init__(self):
        self.score__ = {"lives": 3, "score": 0}
        print(FILE_PATH)
        self.file = open(FILE_PATH, "w")

    def getLives(self):
        return self.score__["lives"]

    def getScore(self):
        return self.score__["score"]

    def save_score(self):
        json_score = json.dumps(self.score__, indent=3)
        self.file.write(json_score)

    def close_file(self):
        self.file.close()

    def add_point(self):
        self.score__["score"] += 1

    def rem_point(self):
        if self.score__["score"] >= 0:
            self.score__["score"] -= 1
        else:
            return False

    def rem_life(self):
        if self.score__["lives"] >= 0:
            self.score__["lives"] -= 1
        else:
            return False

    def add_life(self):
        if (self.score__["lives"] <= 3):
            self.score__["lives"] += 1
        else:
            return False
