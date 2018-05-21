'''
Class for Marker. Stores data pertaining to individual markers
@params x -> X coordinate of the marker
        y -> Y coordinate of the marker
        label -> Label name of the marker
'''
class Marker:

    def __init__(self, x=0, y=0, label="NA"):
        self.x = x
        self.y = y
        self.label = label

    def printCoords(self):
        print("x: {0}, y: {1}, label: {2}".format(self.x, self.y, self.label))

    def printLabel(self):
        print("This is marker: {0}".format(self.label))

