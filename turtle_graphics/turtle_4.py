# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import turtle as t

count = 1
diff = 9

t.pencolor('magenta')
t.width(2)
t.speed(12)

while count <= 360/diff:
    t.circle(50,360)
    t.right(diff)
    
    count+=1
    
t.mainloop()

