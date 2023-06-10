FROM python:3.6

# The environment variable ensures that the Python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the source code into the container at /app
COPY . /app

# Specify the command to run your application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
