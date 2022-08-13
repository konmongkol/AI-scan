#import
import numpy as np
from matplotlib import pyplot as plt
import time
#สร้างฟังชันการทำงาน
def display(maze, i, j):
    img = np.zeros((*maze.shape, 3), dtype = np.uint8)#
    img[maze == '0'] = 255#ตรวจสอบ o เเล้วเปลียนสี
    img[maze == '.'] = [255, 200, 200]#ตรวจสอบ . เเล้วเปลียนสี
    img[maze == 'E'] = [0, 255, 0]#ตรวจสอบ E เเล้วเปลียนสี
    img[i, j] = [255, 0, 0]#เช็ค i,jเเล้วเปลียนสี
    plt.imshow(img)#showรูปดูกค่าจาก image
    plt.axis('off')#ปิดเเกน
    plt.pause(0.01)#ตั้งเวลา
    plt.cla()#เคลียภาพที่ผ่านไปเเล้ว
#สร้างฟังชันการเดินซำ้
def isconnect(a, b):
    i, j = a
    for m, n in zip([i-1, i, i+1, i], [j, j-1, j, j+1]):#เช็คการเดินรอบ
        if m == b[0] and n == b[1]:
            return True
    return False
def stack(a, b):
    i, j = a
    for m, n in zip([i-1, i, i+1, i], [j, j-1, j, j+1]):#เช็คการเดินรอบ  
        if m == b[0] and n == b[1]:
            return True
    return False
#เเผนที่การเดิน
maze = np.array      ([list('1E1111111111111'),
                              list('100011110000001'),
                              list('100000000000001'),
                              list('101111111111111'),
                              list('100000000000001'),
                              list('111011111111001'),
                              list('100001000001001'),
                              list('100100010000001'),
                              list('101000010101101'),
                              list('1000010110000S1'),
                              list('111111111111111') ])

stack = []#
stack2 = []
start = np.where(maze == 'S')#ตรวจค่า sเเละให้s = start
i, j = start[0][0], start[1][0]#เช็คค่าstartเเล้วนำไปใส่ i,j
display(maze, i, j)
path = []#เก็บค่า i,j
times = time.time()#เริ่มนับเวลา
while maze[i, j] != 'E':#เช็คค่าจนกว่าจะเจอ E
    maze[i, j] = '.'#ให้ maze[i, j] = .
    path.append([i, j])#นำค่า i,j ใส่ไปใน path
    for m, n in zip([i-1, i, i+1, i], [j, j-1, j, j+1]):#ให้ m,n เก็บค่าตำเเหน่งรอบๆ
        if maze[m, n] == '0' or maze[m, n] == 'E':#ถ้า maze[m,n] = 0 or maze[m,n] = E
            stack.append([m, n])#เก็บค่าที่เป็น 0
            stack2.append([m, n])
    if len(stack) > 0:#เช็คว่ามีการเก็บข้อมูลstackหรือป่าว
        i, j = stack.pop()#นำค่าออก
    else:
        print('cannot exit!')
        break
    for [I, J] in path[::-1]:#ย้อนค่ากลับ
        if isconnect([i, j], [I, J]): break 
        path.pop()#
        display(maze, path[-1][0], path[-1][1])
    display(maze, i ,j)
print(time.time() - times)#จับเวลาทำงานเสร็จ
print(stack)
