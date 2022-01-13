from xmlrpc.server import SimpleXMLRPCServer


def sum(n):
    sum_till_n = ((n)*(n+1))/2
    return sum_till_n


server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)


print("Listening on port 8000...")

server.register_function(sum, "sum")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Closing or exiting")
