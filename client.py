# client.py  
import socket
import time
import pygame.camera
import base64
import pygame
from pygame.locals import*

stopConnection = 300

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))

while stopConnection:
    #time.sleep(1)        
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 8080

    # connection to hostname on the port.
    s.connect((host, port))                               

    # Receive no more than 1024 bytes
    with open('recieved_file.jpg', 'wb') as image_file:
        print("File opened")
    
        while True:
            encoded_image_data = s.recv(1024)
            print("Recieved: ", encoded_image_data)

            if not encoded_image_data:
                break

            image_file.write(encoded_image_data)

    s.close()    

    img = pygame.image.load('recieved_file.jpg')

    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()

    print("Connection closed")

    stopConnection = stopConnection - 1