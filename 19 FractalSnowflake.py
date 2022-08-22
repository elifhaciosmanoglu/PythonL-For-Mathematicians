import turtle
def kochCurve(t, iterations, length, shorteningFactor, angle):
  if iterations == 0:
    t.forward(length)
  else:
    iterations = iterations - 1
    length = length / shorteningFactor
    kochCurve(t, iterations, length, shorteningFactor, angle)
    t.left(angle)
    kochCurve(t, iterations, length, shorteningFactor, angle)
    t.right(angle * 2)
    kochCurve(t, iterations, length, shorteningFactor, angle)
    t.left(angle)
    kochCurve(t, iterations, length, shorteningFactor, angle)
t = turtle.Turtle()
t.hideturtle()
for i in range(3):
  kochCurve(t, 4, 200, 3, 60)
  t.right(120)
turtle.mainloop()
