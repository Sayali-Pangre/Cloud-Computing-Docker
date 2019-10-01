FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 4000
CMD ["python3","web.py"]
