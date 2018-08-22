
# docker-volume-test

Simple test for executing a Python/TensorFlow script in a Docker container, and using a Docker Volume to acquire file input/output external from the Docker container

Build the image and name it as `volume-test` using the following command:

```bash
docker build -t volume-test .
```

Once the image has been built, run using:

```bash
docker run -it --rm volume-test
```

To use a volume, such that the program saves data to a folder named `dout` on
the host (IE outside the container), use:

```bash
docker run -it --rm -v $(pwd)/dout:/app/dout volume-test
```

~~(In windows, replace `$(pwd)` with `%cd%`)~~

((If using Windows, the "source destination" is on a virtual machine. Have to specify the folder using host_mount, see [here](https://github.com/docker/for-win/issues/1669#issuecomment-366717127)))
