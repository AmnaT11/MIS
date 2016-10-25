class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
my_point = Point()
print(my_point)
my_point.x = 3
my_point.y = 4

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

    print_point(my_point)
    Amna_point = Point()
    Amna_point.x = 100
    Amna_point.y = 200
    print_point(Amna_point)


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    import math
    return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)

my_point = Point()
my_point.x =1
my_point.y =1



class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """
Amna_rect = Rectangle

def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print(('Does box have an attribute x?'), hasattr(box,'x'))

    print(('Does box have an attribute corner?'), hasattr(box, 'corner'))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


    def __str__(self):
        return 'This point is (%g, %g)'.format(self.x, self.y)

    new_point = Point()
    new_point.x = 100
    new_point.y = 50
    print(new_point)