import pygame as pg


class PivotSprite(pg.sprite.Sprite):
    def init(self, image, position, pivot=(0, 0)):
        super().__init__(self)
        self.base_image = image
        self.image = image
        self.rect = image.get_rect(center=position)
        self.origin = pg.Vector2(self.rect.center)
        self.pivot = self.origin - (pg.Vector2(pivot) + self.rect.topleft)
        self.rect.center += self.pivot

    def rotate(self, angle):
        pivot = self.pivot.rotate(angle)
        self.image = pg.transform.rotate(self.base_image, -angle)
        self.rect = self.image.get_rect(center=self.origin + pivot)

    def to_mouse(self, mpos):
        angle = (mpos - self.origin).as_polar()[1]  # Second value is the angle.
        self.rotate(angle)
