# HTTP-Server-using-Steganography

This repo contains a secure HTTP server that is able to serve web clients with secure contents. It uses Python socket programming and Steganography to achieve this task.The server encodes the text file requested by the client in an image using least 3 bits steganography and The client on receipt of the encoded image file, runs the decoder and extracts the .txt file from the image. Detailed explanation can be found here: 
https://wahabaftab.com/L3SB_Steganography/

This server runs on port 55555 and is capable of returning 2 different kinds of responses to its clients:
1. If the request is of the form http://localhost:55555/file1.txt the server will locate the requested file, dynamically encode this file in one of the many images it has and serve this encoded PNG image to the client.
2. If the request to the server is of an unknown page, the server must return an error message to the client browser. Look at the HTTP response message codes 400 and 404.

### How to Run:
1) Run server.py
2) Run client.py
3) Run command prompt and type "ipconfig" to get ipv4 id
4) Run your browser 
5) Enter ip into the url bar followed by ":55555"
6) A page will load
7) Enter filename into the text box
8) Press enter or click on "Get File" button
9) The page will reload, which allows you to enter file name again(double check)
10) Enter your file name again
11) A new page will appear with the encoded image and encoded text will be decoded 
    in client folder.
    
#### Note: 
This project is not maintained and was made in 2016 using Python 2.7, it might run into some issues with newer Python versions or libraries.
