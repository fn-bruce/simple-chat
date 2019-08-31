# simple-chat

This project was created to test my knowledge on multithreading and socket programming in order to create a simple chat client from scratch.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3
macos
```

### Installing

In order to have this working, you're going to need to clone this repo.

Clone to current directory:

```
git clone https://github.com/freshpocky/simple-chat.git
```

## Running the tests

Before testing this on a server, make sure to test this locally. There are some things you'll need to proceed.

### Get current systems IP address

In order to connect to the client to a server, you'll need to know the current devices IP address. Type this into your terminal.

```
ipconfig getifaddr en0
```

### Running server.py

Before we run the client, the server will need to run first. In the same directory of this project, run this command.

```
python3 server.py
```

Enter the port when prompted.

```
What port would you like to use? 5000
```

### Running client.py

After you run the server, you can now run the client. Open another terminal and run this command in the same directory as your project.

```
python3 client.py
```

Enter the IP address you recently received.

```
Host: [YOUR IP ADDRESS HERE]
```

Enter the host your server program is connected to.

```
Port: 5000
```

After that, you should recieve a message on your server program saying that a connection has established. Once that's done, you can follow the same steps to run the client program on another terminal and you should be able to talk between both client programs!
