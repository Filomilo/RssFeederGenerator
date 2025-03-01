FROM python

COPY requirements.txt requirements.txt
RUN pip install -r  requirements.txt
WORKDIR /app
COPY ./app/ /app


# running app 
EXPOSE 5000
ENTRYPOINT [ "gunicorn","--bind","127.0.0.1:5000","app:app" ]