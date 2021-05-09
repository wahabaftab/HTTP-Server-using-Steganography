from socket import *
import time
import os
import random
import sys
from PIL import Image,ImageFilter

# import ImageFilter


def encoder(fn):
    r = random.randint(1, 10)
    if r == 1:
        im = Image.open("1.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 2:
        im = Image.open("2.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 3:
        im = Image.open("3.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 4:
        im = Image.open("4.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 5:
        im = Image.open("5.png").convert('RGB')
        print im.format, im.size, im.mode
    if r ==6:
        im = Image.open("6.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 7:
        im = Image.open("7.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 8:
        im = Image.open("8.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 9:
        im = Image.open("9.png").convert('RGB')
        print im.format, im.size, im.mode
    if r == 10:
        im = Image.open("10.png").convert('RGB')
        print im.format, im.size, im.mode
    X = 0
    Y = 0
    myfile = open(fn)
    text = myfile.read()
    myfile.close()
    length = len(text)
    # im.show()
    for it in range(0, length):
        bnry = ' '.join(format(ord(xx), 'b') for xx in text[it])  # it character is converted to binary
        if len(str(bnry)) != 8:
            temp = 8 - len(str(bnry))
            for x in range(0, temp):
                bnry = '0' + str(bnry)
        else:
            bnry = str(bnry)
        r, g, b = im.getpixel((X, Y))

        if len(str(bin(r))[2:]) != 8:
            temp0 = 8 - len(str(bin(r))[2:])
            r = str(bin(r))[2:]
            for x1 in range(0, temp0):
                r = '0' + (str(r))
        else:
            r = str(bin(r))[2:]

        if len(str(bin(g))[2:]) != 8:
            temp1 = 8 - len(str(bin(g))[2:])
            g = str(bin(g))[2:]
            for x2 in range(0, temp1):
                g = '0' + (str(g))
        else:
            g = str(bin(g))[2:]

        if len(str(bin(b))[2:]) != 8:
            temp2 = 8 - len(str(bin(b))[2:])
            b = str(bin(b))[2:]
            for x3 in range(0, temp2):
                b = '0' + (str(b))
        else:
            b = str(bin(b))[2:]
        if len(str(bin((int(r, 2) & 251) | int(bnry[0], 2))[2:])) != 8:
            tem0 = 8 - len(str(bin((int(r, 2) & 251) | int(bnry[0], 2))[2:]))
            r = str(bin((int(r, 2) & 251) | int(bnry[0], 2) << 2)[2:])
            for y in range(0, tem0):
                r = '0' + r
        else:
            r = str(bin((int(r, 2) & 251) | int(bnry[0], 2) << 2))[2:]

        if len(str(bin((int(r, 2) & 253) | int(bnry[1], 2))[2:])) != 8:
            tem1 = 8 - len(str(bin((int(r, 2) & 253) | int(bnry[1], 2))[2:]))
            r = str(bin((int(r, 2) & 253) | int(bnry[1], 2) << 1)[2:])
            for y in range(0, tem1):
                r = '0' + r
        else:
            r = str(bin((int(r, 2) & 253) | int(bnry[1], 2) << 1))[2:]

        if len(str(bin((int(r, 2) & 254) | int(bnry[2], 2))[2:])) != 8:
            tem2 = 8 - len(str(bin((int(r, 2) & 254) | int(bnry[2], 2))[2:]))
            r = str(bin((int(r, 2) & 254) | int(bnry[2], 2))[2:])
            for y in range(0, tem2):
                r = '0' + r
        else:
            r = str(bin((int(r, 2) & 254) | int(bnry[2], 2)))[2:]

        if len(str(bin((int(g, 2) & 251) | int(bnry[3], 2))[2:])) != 8:
            tem3 = 8 - len(str(bin((int(g, 2) & 251) | int(bnry[3], 2))[2:]))
            g = str(bin((int(g, 2) & 251) | int(bnry[3], 2) << 2)[2:])
            for y in range(0, tem3):
                g = '0' + g
        else:
            g = str(bin((int(g, 2) & 251) | int(bnry[3], 2) << 2))[2:]

        if len(str(bin((int(g, 2) & 253) | int(bnry[4], 2))[2:])) != 8:
            tem4 = 8 - len(str(bin((int(g, 2) & 253) | int(bnry[4], 2))[2:]))
            g = str(bin((int(g, 2) & 253) | int(bnry[4], 2) << 1)[2:])
            for y in range(0, tem4):
                g = '0' + g
        else:
            g = str(bin((int(g, 2) & 253) | int(bnry[4], 2) << 1))[2:]

        if len(str(bin((int(g, 2) & 254) | int(bnry[5], 2))[2:])) != 8:
            tem5 = 8 - len(str(bin((int(g, 2) & 254) | int(bnry[5], 2))[2:]))
            g = str(bin((int(g, 2) & 254) | int(bnry[5], 2))[2:])
            for y in range(0, tem5):
                g = '0' + g
        else:
            g = str(bin((int(g, 2) & 254) | int(bnry[5], 2)))[2:]

        if len(str(bin((int(b, 2) & 251) | int(bnry[6], 2))[2:])) != 8:
            tem6 = 8 - len(str(bin((int(b, 2) & 251) | int(bnry[6], 2))[2:]))
            b = str(bin((int(b, 2) & 251) | int(bnry[6], 2) << 2)[2:])
            for y in range(0, tem6):
                b = '0' + b
        else:
            b = str(bin((int(b, 2) & 251) | int(bnry[6], 2) << 2))[2:]

        if len(str(bin((int(b, 2) & 253) | int(bnry[7], 2))[2:])) != 8:
            tem7 = 8 - len(str(bin((int(b, 2) & 253) | int(bnry[7], 2))[2:]))
            b = str(bin((int(b, 2) & 253) | int(bnry[7], 2) << 1)[2:])
            for y in range(0, tem7):
                b = '0' + b
        else:
            b = str(bin((int(b, 2) & 253) | int(bnry[7], 2) << 1))[2:]
        im.putpixel((X, Y), (int(r, 2), int(g, 2), int(b, 2)))
        X += 1
        if X >= im.size[0] and Y < im.size[1]:
            Y += 1
            X = 0
        if Y == im.size[1]:
            break

            # print r,g,b
    print len(text)
    b_wala = len(text) % 100
    g_wala = int(len(text) / 100) % 100
    r_wala = int(len(text) / 10000)

    r, g, b = im.getpixel(((im.size[0] - 1), (im.size[1] - 1)))
    im.putpixel((im.size[0] - 1, im.size[1] - 1), (r_wala, g_wala, b_wala))
    im.save("encoded.png")
    print r_wala, g_wala, b_wala
    print im.getpixel((im.size[0] - 1, im.size[1] - 1))

def main():
    var='xyz'
    serverPort = 55554
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('0.0.0.0', serverPort))
    serverSocket.listen(40)

    print "Server is ready"

    while 1:
        connectionSocket, clientAddress = serverSocket.accept()
        response = connectionSocket.recv(2048)
        print response
        if os.path.exists(response):
            Ack = "Exists"
            connectionSocket.send(Ack)
            encoder(response)
            size=str(os.path.getsize('encoded.png'))
            connectionSocket.send(size)
            with open('encoded.png', 'rb') as f:
                sendbytes=f.read(2048)
                connectionSocket.sendall(sendbytes)
                print "sending"
                while sendbytes!= "":
                    sendbytes = f.read(2048)
                    connectionSocket.sendall(sendbytes)
        else:
            NACK= 'Not Exist'
            connectionSocket.send(NACK)
            size = str(os.path.getsize('error.png'))
            connectionSocket.send(size)
            with open('error.png', 'rb') as f:
                sendbytes = f.read(2048)
                connectionSocket.sendall(sendbytes)
                print "sending"
                while sendbytes != "":
                    sendbytes = f.read(2048)
                    connectionSocket.sendall(sendbytes)
        connectionSocket.close()
main()








