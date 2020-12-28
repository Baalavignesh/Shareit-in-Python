import tkinter as Tk  
import os
from tkinter import filedialog
import socket
import tqdm

location = '' 
state = 0
person = ''
ip = ''

def SelectFile():
    
    # Initial Variables 
    
    global state
    global person
    global location
    state = 1
    
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname) 
    currdir = os.getcwd()

    # Declaration of Box
    
    empty1 = Tk.Label(root, text = " ")     
    subInfo = Tk.Label(root, text = "Your File Location")
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory', filetype = (("jpeg", "*jpg"), ("All Files", "*.*")))
    FileLocation = Tk.Entry(root, width=50, borderwidth = 2)
    FileLocation.insert(0, tempdir)
    location = tempdir
    print ("You chose: %s" % tempdir)
    subInfo = Tk.Label(root, text = "Share this to your Friend: " + IPAddr)
    empty2 = Tk.Label(root, text = " ")
    empty3 = Tk.Label(root, text = " ")
    Done = Tk.Button(root, text = "Send File", command = root.destroy)
    
    # Alignment of Box
    
    empty1.grid(row = 5, column = 0, columnspan = 4)
    subInfo.grid(row = 6, column = 0, columnspan = 4)
    FileLocation.grid(row = 7, column = 0, columnspan = 4)
    empty2.grid(row = 8, column = 0, columnspan = 4)
    subInfo.grid(row = 9, column = 0, columnspan = 4)
    empty3.grid(row = 10, column = 0, columnspan = 4)
    Done.grid(row = 11, column = 0,  columnspan = 4)



def GetIP():
    
    def enteredIP():
        global ip
        ipAddress = IP.get()
        ip = ipAddress        
        
        
    # Initial Variables 
    global state
    global location
    state = 2
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    
    # Declaration of Box
    
    empty1 = Tk.Label(root, text = " ")
    lable = Tk.Label(root, text = "Destination File Location")
    empty3 = Tk.Label(root, text = " ")
    destination = Tk.Entry(root, width=60, borderwidth = 2)
    destination.insert(0, tempdir)
    location = tempdir
    empty4 = Tk.Label(root, text = " ")    
    IP = Tk.Entry(root, width=50, borderwidth = 2)
    Done1 = Tk.Button(root, text = "First Confirm IP", command = enteredIP)
    subInfo = Tk.Label(root, text = "Enter your Friend's IP Address")
    empty2 = Tk.Label(root, text = " ")    
    Done = Tk.Button(root, text = "Receive File", command = root.destroy)
    empty5 = Tk.Label(root, text = " ")
    
    
    # Alignment of Box
    
    empty1.grid(row = 5, column = 0, columnspan = 4)
    lable.grid(row = 6, column = 0, columnspan = 4)
    empty4.grid(row = 7, column = 0, columnspan = 4)
    destination.grid(row = 8, column = 0, columnspan = 4)
    empty3.grid(row = 9, column = 0, columnspan = 4)
    subInfo.grid(row = 10, column = 0, columnspan = 4)
    IP.grid(row = 11, column = 0, columnspan = 4)
    empty2.grid(row = 12, column = 0, columnspan = 4)
    Done1.grid(row = 13, column = 0)
    Done.grid(row = 13, column = 1)
    empty5.grid(row = 14, column = 0, columnspan = 4)
    
    
# Staring of Code (Tkinter)

root = Tk.Tk()
root.title("FileShare")


def getData():
    top = Tk.Toplevel()
    myLable = Tk.Label(top, text="Summary")
    myLable.grid(row = 0, column = 0)

def NextButton():
    global person
    name = e.get()
    person = name
    Heading = Tk.Label(root, text = "Welcome " + name)
    SubHeading = Tk.Label(root, text = "Start sharing the files")
    Heading.grid(row = 0, column = 0,columnspan = 4)
    SubHeading.grid(row = 3, column = 0,columnspan = 4)
    status = False
    
    #Send and Recieve Button
    
    Send = Tk.Button(root, text = "Send", padx = 50, pady = 10, command = SelectFile)
    Receive = Tk.Button(root, text = "Receive", padx = 50, pady = 10, command = GetIP)
    Send.grid(row = 4, column = 0)
    Receive.grid(row = 4, column = 1)
   
   
    #Call Summary of Code
    if (status == True):
        getData()
        for i in range (0,10):
            print(i)
            
    

myLable1 = Tk.Label(root, text = "Welcome")
e = Tk.Entry(root, width=75, borderwidth = 2)  
e.insert(0, 'Enter your Name:') 
myButton = Tk.Button(root, text = "Next", padx = 50, pady= 10, command= NextButton)
myLable1.grid(row = 0, column = 0,columnspan = 4)
e.grid(row = 1, column = 0, columnspan = 2)
myButton.grid(row = 2, column = 0,columnspan = 4)


Tk.mainloop()

print(person)   #Name of Sender or Receiver
print(state)    #To Run Server or Client Code
print(location) #Destination and File Sending Directiry Location
print(ip)       #IP Address of Server which is written in Client Side



#Server Side
if (state == 1):
    
    print('sending file...')
    #Paste your Server Side Code Here

    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 1024 * 4 #4KB
    
    filename = os.path.basename(location)
    host = socket.gethostbyname(socket.gethostname())
    port = 5001
    
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print("[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    
    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
            # file transmitting is done
                break
            # we use sendall to assure transimission in busy networks
            
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the socket
    s.close()

# Client Side                
elif (state == 2):
    
    print('Receiving file..')
    
    SERVER_HOST = ip
    SERVER_PORT = 5001
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    # create the server socket
    # TCP socket
    s = socket.socket()
    # bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    # accept connection if there is any
    client_socket, address = s.accept() 
    # if below code is executed, that means the sender is connected
    print(f"[+] {address} is connected.")
    
    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(location+"/"+filename, "wb") as f:
        for _ in progress:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    
    # close the client socket
    client_socket.close()
    # close the server socket
    s.close()
    
    
else:
    print('Re-Run the Code, Something went Wrong')