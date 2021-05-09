from socket import *
import time
# import Image
from PIL import Image,ImageFilter

import os
import sys
import random

def main():
    htpre = "<html>\n<head>\n\t<title>\n\t\tTEST\n\t</title>\n</head>\n<body style=\"background-image:url(http://pre00.deviantart.net/7ed3/th/pre/f/2013/170/5/4/linkin_park_logo_wallpaper_hd_by_galaxy244-d69oc5l.jpg)\">\n<button type=\"button\" id=\"button1\" data-loading-text=\"\" class=\"btn btn-primary btn-lg\" autocomplete=\"off\">Decode</button>\n"
    htpost = "\n</body>\n</html>"
    htprerr = "<html>\n<head>\n\t<title>\n\t\tTEST\n\t</title>\n</head>\n<body style=\"background-image:url(http://pre00.deviantart.net/7ed3/th/pre/f/2013/170/5/4/linkin_park_logo_wallpaper_hd_by_galaxy244-d69oc5l.jpg)\">\n"

    name=''
    serverIP = 'localhost'
    serverPort = 55554

    x = 4
    HOST, PORT = '0.0.0.0', 55555

    listen_socket = socket(AF_INET, SOCK_STREAM)
    listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(40)
    print "server is listening"
    htmlheader = "HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n"
    f = open('project.html')
    htmltext = f.read()
    f.close()
    html = htmlheader + htmltext
    while x != 0:
        tempy=''
        leny=0
        x -= 1
        c_connection, c_address = listen_socket.accept()
        request = c_connection.recv(2048)
        c_connection.sendall(html)

        for iterator in range(5,len(request)):
            leny+=1
            if request[iterator]== " ":
                break
        c_connection.close()
        if x==0:
            name = str(request)[12:5+leny-1]
            print str(request)[12:5+leny-1]
            break

        #code to display page 2
    while 1:


        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverIP, serverPort))
        message = name
        clientSocket.send(message)
        Ack = clientSocket.recv(2048)
        print "--->" + Ack
        print "\n"
        filesize = int(clientSocket.recv(2048))
        f = open('output.png', 'wb')
        data = clientSocket.recv(2048)
        totalrec = len(data)
        f.write(data)
        while totalrec != filesize:
            data = clientSocket.recv(2048)
            totalrec += len(data)
            f.write(data)
        clientSocket.close()

        if str(Ack)[0:6] == "Exists":
            X = 0
            Y = 0
            f = open("Decoded.txt", "w")
            im = Image.open("output.png")
            # print im.size
            s1, s2, s3 = im.getpixel(((im.size[0] - 1), (im.size[1] - 1)))
            sizey = (s1 * 10000) + (s2 * 100) + (s3)
            # print sizey
            for it in range(0, sizey):
                r, g, b = im.getpixel((X, Y))
                r = str(bin(r))[2:]
                g = str(bin(g))[2:]
                b = str(bin(b))[2:]
                if len(r) != 8:
                    temp0 = 8 - len(r)
                    for x1 in range(0, temp0):
                        r = '0' + (str(r))
                else:
                    r = r
                if len(g) != 8:
                    temp0 = 8 - len(g)
                    for x1 in range(0, temp0):
                        g = '0' + g
                else:
                    g = g
                if len(b) != 8:
                    temp0 = 8 - len(b)
                    for x1 in range(0, temp0):
                        b = '0' + b
                else:
                    b = b
                char = r[5:] + g[5:] + b[5:7]
                dec = ' '.join(chr(int(char[i:i + 8], 2)) for i in xrange(0, len(char), 8))
                f.write(dec)
                X += 1
                if X >= im.size[0] and Y < im.size[1]:
                    Y += 1
                    X = 0
                if Y == im.size[1]:
                    break
            f.close()
            print 'izz decoded'


        f = open("Decoded.txt", "r")
        tekst = f.read()
        f.close()
        data_uri = open('output.png', 'rb').read().encode('base64').replace('\n', '')
        img_tag = '<img src=\"data:image/png;base64,{0}\" width=\"1350\" height=\"630\">'.format(data_uri)
        p2_connection, p2_address = listen_socket.accept()
        p2req = p2_connection.recv(2048)
        print p2req
        if str(Ack)[0:6]=="Exists":
            p2_connection.sendall(htpre + img_tag + htpost)
        if str(Ack)[0:9]=="Not Exist":
            p2_connection.sendall(htprerr + img_tag + htpost)
        p2_connection.close()

main()

