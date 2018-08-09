
# docker-volume-test

Simple test for executing a Python/TensorFlow script in a Docker container, and using a Docker Volume to acquire file input/output external from the Docker container

Simultaneously build the image, name it as "img" and run in a container using the following command:

`docker build -t img . && docker run -it img`

Once the image has been built, run using:

`docker run -it img`

To use a volume, such that the program saves data to a folder on the host (IE outside the container), use:

``docker run -v `pwd`/dout:/app/dout -it jake-img``
