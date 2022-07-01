import json
import os.path

from retrogame.constants import FILE_PATH


class Score:
    def __init__(self):

        self.__lives=3
        self.file = open(FILE_PATH, "w+")
        self.dictscore = json.load(self.file) if self.file.read() else {"Highscore": 0}

        self.__score = 0

    def getLives(self):
        return self.__lives


    def getScore(self):
        return self.__score

    def save_score(self):
        self.dictscore = json.load(self.file) if self.file.read() else {"Highscore": 0}
        print(self.__score, self.dictscore["Highscore"])
        if self.__score > self.dictscore["Highscore"]:
            print("cond")
            self.dictscore["Highscore"] = self.__score

        json.dump(self.dictscore, self.file)

    def close_file(self):
        self.file.close()

    def add_point(self):
        self.__score += 1

    def rem_point(self):
        if self.__score >= 0:
            self.__score -= 1
        else:
            return False

    def rem_life(self):
        if self.__lives >= 0:
            self.__lives -= 1
        else:
            return False

    def add_life(self):
        if self.__lives <= 3:
            self.__lives += 1
        else:
            return False
