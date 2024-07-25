# base image for building the Flask container
FROM python:3.10-alpine
# working directory where the Docker container will run. 
# Note: originally, with EC2 setup, deployed the app to run from /flaskapp/helloec2rdsipaddress.  
# ...Not the case with this container impementation.
WORKDIR /helloec2rdsipaddress 
# Copying all the application files to the working directory
COPY . /helloec2rdsipaddress/
# Install all the dependencies required to run the Flask application
RUN pip install -r requirements.txt
# Expose the Docker container for the application to run port
EXPOSE 8080
# The command required to run the Dockerised application
CMD ["python", "/helloec2rdsipaddress/app.py"]