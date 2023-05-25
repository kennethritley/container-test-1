# Fun with Docker Containers!

This is a little learning exercise so you can find out how you can get containers to
talk to each other (a private network) and to talk to you.

## Table of Contents

- [Installation](#installation)
- [Javadocs](#javadocs)
- [Authors](#authors)
- [License](#license)
- [CHANGELOG.md](CHANGELOG.md)


## Changelog

For a detailed list of changes and version history, please refer to the [CHANGELOG.md](CHANGELOG.md) file.

## Installation

See the Miro board (https://miro.com/app/board/uXjVMGaexY0=/?share_link_id=854079158690) for full details and screenshots, but here is a brief summary.

To build the images from the Python apps:
- docker build -t input -f Dockerfile.input .
- docker build -t server -f Dockerfile.server .

To create the private Docker network that let's containers talk to one another:
- docker network create mynetwork

To run the containers from the images:
- docker run --network=mynetwork --name=input -it input
- docker run --network=mynetwork --name=server server

And to clean everything up when you are done:
stop the containers
- docker stop input server
- docker rm input server
- docker image rm input server
- docker network rm mynetwork

## Javadocs

Javadocs are the built-in documentation system in Java, so that with one
command you can create beautiful HTML files that show your source code
documentation.

This application does NOT use Javadocs

## Authors

Your friendly, neighborhood Dr. Ken and his little green friend

## License

Never operate a motor vehicle without the proper license.
