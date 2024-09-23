## Pathfindr Assignment

The requirements document can be found as `Pathfind Assignment.pdf`

### Notes
* For caching redis is used
* Add your amadeus api key and secret in .env


*The recommended installation is via docker compose.*
### Local Installation:
1. Consider creating a separate python environment for this installation, although it is not necessary, but recommeded.
2. run `pip install -r requirements.txt`
3. run `python manage.py runserver`

#### Dependencies:
A redis server, can be local or server, change the env parameters according to your redis setup

### Docker Installation:
#### Docker Only
 The docker file can be ran directly but need to change, redis host to be pointed at `host.docker.internal`, build the image `docker build -t pathfind-assignment .` and run `docker run -p 8000:8000 pathfindr-assignment`.
#### Docker Compose
1. The docker compose installation is recommended one, and standalone too. just run `docker compose up` to see logs, or with `-d` flag to keep your terminal clean.

This will bring up redis and the assignment api, not requirement for edting anything, although you can still point to redis if it is running on server, just open `docker-compose.yml` and change the `REDIS_HOST`, `REDIS_PORT` and `REDIS_DB`.

### .env
The dot env file contains all the data that is required by application to work, or tune-in some features, like caching

### What's Next:
The app seems pretty much done, but it can be further improved in following areas.
1. Templatized and use of constants for logging messages.
2. More set of exceptions dealing with wide variety of errors.
3. Unit testing for the whole app.

At last i do not want to stretch this further, I completed the assignment by adhereing all the mentioned requirements, Thank you for your support and consideration.

Do let me know if anything fails


