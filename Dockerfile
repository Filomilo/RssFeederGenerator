FROM python

COPY requirements.txt requirements.txt
RUN pip install -r  requirements.txt
WORKDIR /app
COPY ./app/ /app


# running app 
EXPOSE 10000 
ENTRYPOINT [ "gunicorn","--bind","0.0.0.0:10000 ","app:app" ]