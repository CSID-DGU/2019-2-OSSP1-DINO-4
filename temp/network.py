import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.43.237'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            #보내고자 하는 정보 전송
            self.client.send(str.encode(data))
            #reply 받음
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)
