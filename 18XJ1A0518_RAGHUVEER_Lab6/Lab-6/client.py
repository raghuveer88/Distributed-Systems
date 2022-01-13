import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("sum of first 3 numbers is {}".format(proxy.sum(3)))
    print("sum of first 10 numbers is {}".format(proxy.sum(10)))
