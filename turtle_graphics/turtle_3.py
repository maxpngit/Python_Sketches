# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t

count = 1
diff = 9
t.pencolor('red')

while count <= 360/diff:
    x = 1
    while x <= 4:
        t.forward(100)
        t.right(90)
        x += 1
        
    t.right(diff)
    count += 1

t.mainloop()
