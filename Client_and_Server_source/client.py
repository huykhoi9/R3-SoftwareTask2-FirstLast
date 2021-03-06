#Huy Khoi Nguyen 500954699
import pygame
import socket

#initialize the speed of rover
speed = 5

#create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the port
s.connect((socket.gethostname(), 5555))

msg = s.recv(1024)
print(msg.decode("utf-8"))

#2: Initiate pygame
pygame.init()
#pygame.font.init()
pygame.display.set_mode((500,500))

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #press Up send that to the server
            if event.key == pygame.K_UP:
                s.send(bytes(f"[f{speed}][f{speed}][f{speed}][f{speed}]", "utf-8"))
            #press Down and send
            if event.key == pygame.K_DOWN:
                s.send(bytes(f"[r{speed}][r{speed}][r{speed}][r{speed}]", "utf-8"))
            #press Left and send
            if event.key == pygame.K_LEFT:
                s.send(bytes(f"[r{speed}][r{speed}][f{speed}][f{speed}]", "utf-8"))
            #press Right and send
            if event.key == pygame.K_RIGHT:
                s.send(bytes(f"[f{speed}][f{speed}][r{speed}][r{speed}]", "utf-8"))
            #change the speed of the rover
            if event.key == pygame.K_1:
                speed = (1/5)*255
            if event.key == pygame.K_2:
                speed = (2/5)*255
            if event.key == pygame.K_3:
                speed = (3/5)*255
            if event.key == pygame.K_4:
                speed = (4/5)*255
            if event.key == pygame.K_5:
                speed = 255
pygame.quit()
