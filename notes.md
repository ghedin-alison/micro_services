# Important

 - to start the docker container with dockerfile and docker-compose
```unix
docker-compose up
```

## Create the app products
 - after start and stop the dbdata, access the docker container by another terminal.
 - don't stop the main container at another terminal
```unix
docker-compose exec backend sh
```
 - create the app product
```unix
python manage.py startapp products
```
 - Now, the directory products will appear on microservices.