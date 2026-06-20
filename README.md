# Three-Flask-Containers-Project

## Architecture

```text
                User
                  |
                  v
      -------------------------
      |         Docker        |
      |        Network        |
      -------------------------
         |       |       |
         v       v       v
      Flask1  Flask2  Flask3
      :3001   :3002   :3003

             |
             v
        Docker Volume
```

## Access Applications

### Flask Application 1

```text
http://localhost:3001
```

### Flask Application 2

```text
http://localhost:3002
```

### Flask Application 3

```text
http://localhost:3003
```

## Container Flow

1. User accesses the application through a browser.
2. Requests are sent to one of the exposed ports:

   * Port 3001 → Flask Container 1
   * Port 3002 → Flask Container 2
   * Port 3003 → Flask Container 3
3. All containers are connected through a Docker network.
4. Containers can communicate with each other using container names.
5. Application data is stored in a Docker volume for persistence.
6. The container processes the request and returns the response to the user.

## Docker Compose Deployment

```bash
docker compose build
docker compose up -d
docker ps
```
