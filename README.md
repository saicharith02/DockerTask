
## Building the Docker Image

To build the Docker image for the Flask app, run the following command:

```sh
docker build -t flask_docker_app .
```
## Building the Docker Container with Volumes
```sh
docker run -d -p 5000:5000 -v /users/saicharith.am/documents/pythonc1/data:/app/data flask_docker_app
```
Now the changes in data.txt in container will also change the data.txt in host machine also.

