# This file is part of Stoneworks (Sishya Hacks D.A.V.).

# Stoneworks (Sishya Hacks D.A.V.) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Stoneworks (Sishya Hacks D.A.V.) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Stoneworks (Sishya Hacks D.A.V.).  If not, see <https://www.gnu.org/licenses/>.

import json
import os.path

from retrogame.constants import FILE_PATH


LEVEL_1 = 20
LEVEL_2 = 50
LEVEL_3 = 75

class Score:
    def __init__(self):

        self.__lives=3
        # self.file = open(FILE_PATH, "w+")
        self.level = 0
        

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
    
    def get_level(self):
        return self.level
    
    def level_up(self):
        self.level += 1
    
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
        if self.score >= LEVEL_3:
            self.level = 3
        elif self.score >= LEVEL_2:
            self.level = 2
        elif self.score >= LEVEL_1:
            self.level = 1

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
