#import LED_I2C_Interface as LED

import LED_Util as LED

import SimpleHTTPServer
import SocketServer
import cgi
import threading



class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):


    def do_GET(self):
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


    def do_POST(self):

        if self.path == '/turn_full_on':
            LED.RED.write(15)
            LED.GREEN.write(15)
            LED.BLUE.write(15)

        if self.path == '/turn_full_off':
            LED.RED.write(0)
            LED.GREEN.write(0)
            LED.BLUE.write(0)

        if self.path == '/turn_on':
            LED.on()

        elif self.path == '/turn_off':
            LED.off()

        elif self.path == '/red_set':
            value = 0
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            for key in form.keys():
                variable = str(key)
                value = str(form.getvalue(variable))

            LED.RED.write(value)

        elif self.path == '/green_set':
            value = 0
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            for key in form.keys():
                variable = str(key)
                value = str(form.getvalue(variable))

            LED.GREEN.write(value)

        elif self.path == '/blue_set':
            value = 0
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            for key in form.keys():
                variable = str(key)
                value = str(form.getvalue(variable))

            LED.BLUE.write(value)

        elif self.path == '/red_toggle':
            LED.RED.toggle()

        elif self.path == '/green_toggle':
            LED.GREEN.toggle()

        elif self.path == '/blue_toggle':
            LED.BLUE.toggle()

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def webserver():
    PORT = 8000
    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("192.168.0.109", PORT), Handler)
    print ("serving at port", PORT)
    httpd.serve_forever()



webserver()



