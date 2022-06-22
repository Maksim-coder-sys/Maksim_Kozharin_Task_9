class Road:
    ASPHALT_MASS = 25
    THICKNESS = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def gross_weight(self):
        gross_w_eight = self._length * self._width * Road.ASPHALT_MASS * Road.THICKNESS/1000
        print(f'{gross_w_eight} т.')

r = Road(5000,20)
r.gross_weight()