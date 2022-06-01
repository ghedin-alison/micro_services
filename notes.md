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
 - Add publish method on views
 - Create a consumer.py file
 - up docker-compose
 - access docker container
```unix
docker-compose exec backend sh
```
- activate the consumer
```unix
python consumer.py
```

 - The communication between the two projects its working. Tests @postman.

### Update Dockerfile to keep only one consumer tab
 - update the Dockerfile and docker-compose to get ready when compose starts
 - As the docker files were updated run:
```unix
docker-compose up --build
```
 - A lot of issues related to access .dbdata. This is because docker was trying to access.
 - To solve this docker problem, just create a .dockerignore and add the folder.

 - Then restart again the server and run this to start db
```unix
docker-compose up -d db
```
