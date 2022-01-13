# Distributed-Systems

### **Problem Statements for each lab are given below**

## LAB - 2

1) Implement echo client server communication using UDP.  (Observe the difference in this program with TCP implementation) <br/>
2) Create a multi-user group chat application using TCP. Your implementation will have one TCP server running, and multiple clients will connect to the server. Message sent by a client should be displayed to all other clients connected to the TCP server. <br/> 
**Use threads to create separate sockets for clients. DONT use python 'select' library to read, and write from the sockets.<br/>**


## LAB - 3

write a program to achieve one-one communication among N Clients connected to a Server. A message from sender client intended to a receiver client has to be transferred only to the receiver client.


## LAB - 4

write a socket program to demonstrate Multicast communication, where a message from the sender is delivered to multiple recipients that belongs to a multicast group. 
You may require two machines to demonstrate the multicast functionality. You can create virtual machines(VMs) in your machine or physical machines in the lab.


## LAB - 5

**Using mpi4py, write the following MPI programs**

1) Matrix addition <br/>

2) Matrix multiplication <br/>

For programs 1 and 2, Use MPI send/receive/broadcast operations where ever required. <br/>

3) Sum of array. (Explore reduce operation) <br/>

4) Explore scatter and gather primitives in MPI programming and write simple programs which uses them. Also, try to use asynchronous versions of the different MPI methods and observe the difference. <br/>

**Note** - You need to install mpi4py and Do not write the entire logic in one process in the MPI program to display the required output (Parallelize your code). <br/>


## LAB - 6

Write client and server programs to demonstrate Remote Procedural Call (RPC) using XML-RPC package. Use XML-RPC python client and server modules. Explore different options provided by the client and server modules.<br/>

## LAB - 7

Use multiprocessing python package to write the below programs.<br/>

a) Inter-process Communication using shared memory.<br/>

Write a program to demonstrate the updation/manipulation of shared dictionary objects between two processes.<br/>
(Use Manager() module (https://docs.python.org/3/library/multiprocessing.html), that creates a server process which holds python objects and allows different other processes to manipulate them)<br/>

(Also explore Array and Value objects, that are generally used to share data between processes - Not flexible to share other python objects).<br/>

b) Basic inter-Process Communication.<br/>

c) Write a program to demonstrate the inter-process communication using a) Pipe and b) Queue.<br/>

## LAB - 8

Explore RabbitMQ server, an open source message broker ( a means of achieving Indirect Communication). As part of this lab, you will install RabbitMQ Server, and Pika (a python client that communicates with server).<br/> 

You are supposed to demonstrate the working of Publish/Subscribe, and Work queues paradigms using RabbitMQ.<br/>

The tutorial of RabbitMQ is available at https://www.rabbitmq.com/getstarted.html.<br/>








