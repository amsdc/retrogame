import json
from retrogame.constants import FILE_PATH


class Score:
    def __init__(self):
        self.score = {"lives": 3, "score": 0}
        self.file =  open(FILE_PATH, "w")

    def getLives(self):
        return self.score["lives"]

    def getScore(self):
        return self.score["score"]

    def save_score(self):
        json_score = json.dumps(self.score, indent=3)
        self.file.write(json_score)

    def close_file(self):
        self.file.close()

    def add_point(self):
        self.score["score"] += 1

    def rem_point(self):
        if self.score["score"] >= 0:
            self.score["score"] -= 1
        else:
            return False

    def rem_life(self):
        if self.score["lives"] >= 0:
            self.score["lives"] -= 1
        else:
            return False

    def add_life(self):
        if (self.score["lives"] <= 3):
            self.score["lives"] += 1
        else:
            return False
