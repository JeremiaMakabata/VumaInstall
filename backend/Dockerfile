# Use an official Python runtime as a parent image
FROM python:3.7

# set the environment
ENV PYTHONUNBUFFERED 1



# Create a directory for  our code
RUN mkdir /VumaInstall/backend

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR /VumaInstall/backend

# Install Python dependencies
COPY requirements.txt /VumaInstall/backend
RUN pip3 install --upgrade pip -r requirements.txt

# Add the rest of the code
COPY . /VumaInstall/backend

