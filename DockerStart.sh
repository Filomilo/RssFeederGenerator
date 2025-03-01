docker build . -t filomilo/rssfeeder  
docker run -p 10000:10000  --net=host filomilo/rssfeeder 