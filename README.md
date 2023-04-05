# restAPI
Dockerize python Flask API

### Install
Simply run
```bash
make install
```
which builds a Docker container with the REST-API python application inside.

### How to use
Have a look in the `Makefile`, but you can try it by running
```bash
make start
make curl
```
which should start the Docker container, and send a simple example of a successful API call.

To kill the Docker container, simply run
```bash
make stop
```
