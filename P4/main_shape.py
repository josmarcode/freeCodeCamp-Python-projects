from shape_calculator import Rectangle, Square

rect = Rectangle(10, 5)

rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(1)
print(sq.get_diagonal())
sq.set_side(5)
print(sq)
sq.set_width(3)
print(sq.get_picture())

print(rect.get_amount_inside(sq))
