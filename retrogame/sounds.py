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

import pygame

pygame.mixer.init()
stone_sound = pygame.mixer.Sound("audio/stone.mp3")
heart_sound = pygame.mixer.Sound("audio/heart.mp3")
apple_sound = pygame.mixer.Sound("audio/apple.wav")
back_sound = pygame.mixer.Sound("audio/menu-backsound.mp3")