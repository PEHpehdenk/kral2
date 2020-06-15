# Copyright (c) 2020 Roman Trapeznikov
from __future__ import annotations

from typing import TYPE_CHECKING

from kral2.game import Vec2

if TYPE_CHECKING:
    pass


class GameObject:
    def __init__(self, pos: Vec2, width, height, color, activity=None, collide=True):
        self.id = None
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.died = False
        self.activity = activity
        self.collide = collide

    def postinit(self):
        pass

    def die(self):
        self.died = True

    def update(self):
        if self.pos.len() > 10000:
            self.die()

    def move(self, pos: Vec2):
        for _pos in (Vec2(pos.x, 0), Vec2(0, pos.y)):
            self.pos += _pos  # Add collision check
            if self.activity:
                if self.activity.is_collide_any(self):
                    self.pos -= _pos

    def to_dict(self):
        return {'id': self.id, 'type': 'GameObject',
                'pos': self.pos.to_dict(), 'width': self.width, 'height': self.height,
                'color': self.color}
