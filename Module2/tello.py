import time
from stats import Stats

class Tello:
    def __init__(self):
        self.local_ip = ''
        self.local_port = 8889
        
        # socket for receiving command
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.local_ip, self.local_port)

        # thread for receiving command ack
        self.receive_thread = threading.Thread(target=self.__receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        # connect tello
        self.tello_ip = '192.168.10.2'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []

        self.MAX_TIME_OUT = 15.0

    def send_command(self.command):
        self.log.append(Stats(command, len(self.log)))

        self.socket.sendto(command.encode('utf-8'), self.tello_address)
        print 'sending command: %s to %s' % (command, self.tello_ip)

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now-start
            if diff > self.MAX_TIME_OUT:
                print 'Max timeout exceeded'
                return
        print 'Done!'

    def __receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('from %s: %s' % (ip, self.response))

                self.log[-1].add_response(self.response)
            except socket.error, exc:
                print 'error occured!'
    
    def on_close(self):
        pass

    def get_log(self):
        return self.log

