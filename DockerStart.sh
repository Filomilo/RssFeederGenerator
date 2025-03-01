docker build . -t filomilo/rssfeeder  
docker run -p 5000:5000 --net=host filomilo/rssfeeder 