def default_content():
    return """
        <h1>ESP8266</h1>
    """

def server(content=default_content):
    import socket, sys, time
    port = 8000
    while True:
        try:
            addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
            s = socket.socket()
            s.bind(addr)
            s.listen(1)
            break
        except OSError:
            port += 1
            time.sleep(1)
    print('listening on', addr)
    while True:
        try:
            cl, addr = s.accept()
        except KeyboardInterrupt:
            print('terminated')
            s.close()
            sys.exit()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            if "HTTP/1." in line:
                print(line)
        cl.send("HTTP/1.1 200 OK\r\n")
        cl.send("Content-Type: text/html\r\n")
        cl.send("\r\n")
        cl.send("<!DOCTYPE html><html> <head> <title>ESP8266</title> </head> <body>")
        cl.send(content())
        cl.send("</body></html>")
        cl.close()
