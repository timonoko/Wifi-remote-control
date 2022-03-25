
import network,time,machine,sys

print('toimii3')

try:
  import usocket as socket
except:
  import socket

clock = machine.Pin(1, machine.Pin.OUT)
data = machine.Pin(3, machine.Pin.IN)
latch = machine.Pin(0, machine.Pin.OUT)

clock.value(0)

def lue():
    latch.value(1)
    clock.value(0)
    clock.value(1)
    clock.value(0)
    latch.value(0)   
    tulos=0
    for x in range(0,9):
        if data.value()==0:
            if tulos==8:
                return 9
            else:
                return 8-tulos
        tulos+=1
        clock.value(0)
        clock.value(1)
    return 0

def nappi():
    loppu=20/0.05
    aika=0
    prevn=0
    while True:
        n=lue()
        if n>0:
            prevn=n
            aika+=1
        elif aika>2:
            return (prevn,aika)
        else:
            aika=0
        time.sleep(0.05)
        loppu-=1
        if loppu==0:
            machine.deepsleep()

NAPPI="TYHJA"
    
def Paina():
    n=nappi()
    if n[1]<15:
        return "ON:"+str(n[0])
    else:
        return "OFF:"+str(n[0])

def web_page():
    html = """
     <html><head> 
     <title>KAUKO</title>
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="icon" href="data:,">
     <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #bd4141; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #5d9868;}</style>
     </head>
      <body>
     <h1>KAUKO</h1> 
     <a href="/"""+NAPPI+""""> <button class="button">"""+NAPPI+"""</button></a> <p> 
     </body>
   </html>"""
    return html



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
  
while True:
    s.settimeout(0.2)
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        s.settimeout(5.0)
        for r in range(1,10):
            if request.find('/ON:'+str(r)) == 6:
                NAPPI=""
            if request.find('/OFF:'+str(r)) == 6:
                NAPPI=""
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError:
        NAPPI=Paina()
        clock.value(0)
        print(NAPPI)

                  
