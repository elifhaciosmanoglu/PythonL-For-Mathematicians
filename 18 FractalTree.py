import turtle
minimumBranchLength = 5
def buildTree(t, branchLength, shortenBy, angle):
  if branchLength > minimumBranchLength:
    t.forward(branchLength)
    newLength = branchLength - shortenBy
    t.left(angle)
    buildTree(t, newLength, shortenBy, angle)
    t.right(angle * 2)
    buildTree(t, newLength, shortenBy, angle)
    t.left(angle)
    t.backward(branchLength)
tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color('green')
buildTree(tree, 50, 5, 30)
turtle.mainloop()
