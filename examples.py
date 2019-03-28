# Copyright (C) 2019  Davide De Tommaso
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>

from checkerboard import Checkerboard

# Default checkerboard: 6x8 inner corners, 7 row x 9 columns
Checkerboard().run()

# Custom checkerboard: 2x2 inner corners, 3 row x 3 columns
#Checkerboard(row_corners=2, col_corners=2).run()

# Custom checkerboard: 9x13 inner corners, 10 row x 14 columns, bg_color=red,
#  and it displays on the screen with id=1 in a multiple screen configuration
#Checkerboard(row_corners=9, col_corners=13, padding_min=50, screen_id=1, bg_color=(255, 0, 0)).run()
