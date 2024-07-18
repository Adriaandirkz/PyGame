


class Sprite:
    droids = []
    bullets = []
    turrets = []
    shockwaves = []

    def update(self):
        pass

    def draw(self):
        pass

    def collision_detector(self, objs):
        for obj in objs:
            distance = self.distance(obj)
            if distance < self.width + obj.width + 5 / 2:
                obj.collision()
                self.collision()

    def distance(self, obj):
        distance = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
        return distance
