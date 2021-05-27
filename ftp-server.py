from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("kali", "kali", "/tmp/", perm="elradfmw")                   # Username - kali, Password - kali, Directory - /tmp/
authorizer.add_anonymous("/tmp/", perm="elradfmw")                              # Directory - /tmp/
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
