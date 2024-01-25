
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11.4

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


# Set the working directory to /disruptiveapi
WORKDIR /disruptiveapi

# © Kyle Olson/Future Trick 2023
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000
                                                           
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


