I Have Used the Docker CLI Commands
For the Building the images
--docker build -t flask_docker_app .
Now running the image with volume we will 
--docker run -d -p 5000:5000 -v /users/saicharith.am/documents/pythonc1/data:/app/data flask_docker_app
Now the changes in data.txt in container will also change the data.txt in host machine also.
