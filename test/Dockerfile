FROM python:3.9-alpine
WORKDIR /srv/app
ADD . /srv/app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/srv/app/test.py"]