#base image of python 3.5 from Docker hub
FROM python:3.5
#set WORKING directory in cotainer
WORKDIR /app
#ADD the current python source file in
#context to host to the cotainer
ADD . /app
#run python application
CMD ["python3", "cal.py"]
