FROM python:3.10.0-alpine3.14

# install dependencies for build
RUN apk add rust cargo

# in case of many dependencies, we can use requirement.txt
RUN pip3 install germansentiment

# add the script to the image on the root directory
ADD app.py /app.py

# run the python script when we run the container 
ENTRYPOINT ["python3", "/app.py"]