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

# Access trouble with docker

I don't know if this will cause security problems, but this was the only way 
to let the file available. Should confirm with a senior. 
```unix
chmod -R 777 ./
```


# Makemigrations
```unix
python manage.py makemigrations
```
```unix
python manage.py migrate
```

### To find the users from db remember to save the database at the IDE.


 - After set the main project, return to this one and set the rabbitmq.
 - Create a producer.py file
