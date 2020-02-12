import turtle as t

count = 0
length = 10

t.pencolor('green')

while count < 20:
    if (count < 10):
        t.left(90)
        t.forward(length)
    else:
        t.pencolor('purple')
        t.right(90)
        t.forward(length)
    length += 10
    count += 1

t.mainloop()