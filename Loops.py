import numpy as np
import random

num_prisioners = 100

prisioners = [x for x in range(0, num_prisioners)]
boxes = list(prisioners)
random.shuffle(boxes)

box_assignment = list(zip(prisioners, boxes))

loop = list()
loops = list()
lens = list()

run_inner = True
run_outer = True

while run_outer:

    next_box = box_assignment[0][0]
    run_inner = True
    loop.clear()

    while run_inner:

        node = [box for box in box_assignment if box[0] == next_box]

        if len(node) == 0:
            run_inner = False
        else:
            loop.extend(node)
            next_box = node[0][1]
            box_assignment.remove(node[0])

    if len(box_assignment) == 0:
        run_outer = False

    loops.append(list(loop))
    lens.append(len(loop)) 

print(loops)
print(lens)
