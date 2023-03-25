FROM python:3.9.16-slim-buster

# Create a directory inside the image for your app
WORKDIR /myapp1

# Copy the contents of myapp (local) to the image
COPY myapp1 .

# Install the requirements for this Python app
RUN pip install -r requirements.txt

# Informs Docker that the running application listens on port 8000
# If not combined with -p (publish), the port will only be accessible from
# inside the container
# https://stackoverflow.com/questions/22111060/what-is-the-difference-between-expose-and-publish-in-docker
EXPOSE 8000

# Run the web server (ASGI)
# By default the web server will bind to the local machine (127.0.0.1 /
# localhost)
# https://pythonspeed.com/articles/docker-connection-refused/
CMD uvicorn main:app --host 0.0.0.0
