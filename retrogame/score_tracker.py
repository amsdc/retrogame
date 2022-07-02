import json
import os.path

from retrogame.constants import FILE_PATH


class Score:
    def __init__(self):

        self.__lives=3
        # self.file = open(FILE_PATH, "w+")
        

        self.score = 0
        self.create_file_if_not_exists()
        self.open_file()

    def create_file_if_not_exists(self):
        if not os.path.isfile(FILE_PATH):
            open(FILE_PATH, "w").close()
    
    def open_file(self):
        self.file = open(FILE_PATH, "r")
        try:
            self.more = int(self.file.read())
        except:
            self.more = 0


    def getLives(self):
        return self.__lives


    def getScore(self):
        return self.score
    
    def get_max_score(self):
        return self.more

    def save_score(self):
        if self.score > self.more:
            self.more = self.score
            
        with open(FILE_PATH, "w") as fh:
            fh.write(str(self.more))

    def close_file(self):
        self.file.close()

    def add_point(self):
        self.score += 1

    def rem_point(self):
        if self.score >= 0:
            self.score -= 1
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
