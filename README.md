# Sentiment-Analysis-Docker
Encapsulation of a sentiment analysis model as a microservice in Docker
## how to create the image

  
1. Our docker image is based on alpine distribution with python 3.10 and pip
``
FROM python:3.10.0-alpine3.14
``

2. Install rust and cargo dependencies for build
    `` bash
 RUN apk add rust cargo
  ``
  
3. install germansentiment pakage
``bash
RUN pip3 install germansentiment
``

4. add the script to the image on the root directory
``bash
ADD app.py /app.py
``

5. run the python script when we run the container
``bash
ENTRYPOINT ["python3", "/app.py"]
``

6. build the image
``bash
docker build . --tag laajailia_image:v1.0
``

## how to use the endpoint

``bash
docker run --rm laajailia_image:v1.0 texts``
texts: list of strings.

## how to deploy on the cloud
it depends on the CI/CD tool so it can be: 
- gitlab-ci (gitlab-ci.yaml: where you configure the deploy steps) 
- github action 
- jenkins
