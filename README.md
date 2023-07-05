 # Cyber-Bytezz-RAT

## Remote Access Trojan (RAT)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This project implements a Remote Access Trojan (RAT) that allows for remote command execution on a client machine. It consists of two components: a client-side code that connects to an attacker server, and a server-side code that listens for incoming connections and executes commands on the client.

The main purpose of this project is to demonstrate how a RAT can be implemented for educational purposes. It highlights the communication between the client and server over a TCP/IP network and the execution of commands on the client's machine.

---

## Features

- Establishes a TCP/IP connection between the client and the attacker server.
- Allows the attacker to send commands to the client machine for execution.
- Executes commands using the `subprocess` module and sends the output back to the attacker.
- Supports the "exit" command to terminate the connection gracefully.

---

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.7 or above).
3. Install the required dependencies by running the command: `pip install -r requirements.txt`.

---

## Usage

1. Start the attacker server by running the server-side code: `python server.py`.
2. Modify the `attacker_ip` variable in the client-side code (`client.py`) to match the IP address of the attacker server.
3. Run the client-side code on the target machine: `python client.py`.
4. The client will connect to the attacker server and wait for commands.
5. On the server-side, enter commands to be executed on the client machine.
6. View the output of the executed commands in the server console.

---

## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request, explaining the changes you have made.

---
## THIS REPOSTIERY STILL UNDER CONSTRUCTION

## HAPPY HACKING !!!!!!!!!!!!!!!!!
