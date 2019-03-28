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

import pyglet

class Checkerboard(pyglet.window.Window):

    def __init__(self, row_corners=6, col_corners=8, padding_min=0, screen_id=0, bg_color=(255, 255, 255), *args, **kwargs):
        display = pyglet.window.get_platform().get_default_display()
        screens = display.get_screens()
        screen = screens[screen_id]
        super(Checkerboard, self).__init__(fullscreen=True, screen=screen, *args, **kwargs)
        self.__row_corners__ = row_corners
        self.__col_corners__ = col_corners
        self.__row_squares__ = self.__row_corners__ + 1
        self.__col_squares__ = self.__col_corners__ + 1
        self.__offset_y__ = padding_min
        self.__bg_color__ = bg_color
        self.__square_size__ = (self.screen.height - 2*self.__offset_y__)/self.__row_squares__
        if self.__square_size__*self.__row_squares__< self.screen.height:
            self.__offset_y__ = (self.screen.height - self.__square_size__*self.__row_squares__)/2
        self.__offset_x__ = (self.screen.width - self.__square_size__*self.__col_squares__)/2
        self.__colors__ = [(0, 0, 0), (255, 255, 255)] # BLACK, WHITE
        self.__corners_xy__ = []

        if self.__square_size__*self.__col_squares__ > self.screen.width:
            raise Exception('The number of column squares exceeds the resolution of the screen')
        elif self.__square_size__*self.__row_squares__ > self.screen.height:
            raise Exception('The number of rows squares exceeds the resolution of the screen')

    def __addQuad__(self, batch, group, x1, y1, x2, y2, rgb_color=(0, 0, 0)):
            batch.add(4, pyglet.gl.GL_POLYGON, group,
                                ('v2i', (x1, self.screen.height-y1, x2, self.screen.height-y1, x2, self.screen.height-y2, x1, self.screen.height-y2)),
                                ('c3B', rgb_color * 4) )

    def on_draw(self):
        self.clear()
        batch = pyglet.graphics.Batch()
        background = pyglet.graphics.OrderedGroup(0)
        self.__addQuad__(batch, background, 0, 0, self.screen.width, self.screen.height, self.__bg_color__)
        for row in range(0, self.__row_squares__):
            for col in range(0, self.__col_squares__):
                group = pyglet.graphics.OrderedGroup(1 + row*self.__col_squares__ + col)
                color = self.__colors__[(col+row) % 2]
                x = self.__offset_x__ + col*self.__square_size__
                y = self.__offset_y__ + row*self.__square_size__
                if row > 0 and col > 0:
                    self.__corners_xy__.append([x, y])
                rect = (x, y, self.__square_size__, self.__square_size__)
                self.__addQuad__(batch, group, x, y, x + self.__square_size__, y + self.__square_size__, color)
        batch.draw()

    def get_corners_xy(self):
        return self.__corners_xy__

    def run(self):
        pyglet.app.run()
