# WebXiv

Personal NGINX web server and web archive running in a Docker container.


Currently hosted at [http://alussana.xyz/](http:/alussana.xyz/).

## Start WebXiv

* Install [Docker](https://www.docker.com/)

* Choose a path that you want to be reachable from the WWW.

  ```
  VOLUME_DIR=/your/files/
  ```

* Choose a path where to create inbox.txt; messages coming from the website will be stores here.

  ```
  INBOX_DIR=/your/files/inbox/
  ```

* Choose a port where the server will be exposed on (replace `8080` with the desired port).

  ```
  $PORT=8080
  ```

* Clone this repository, build and run the docker image.

  ```
  git clone https://github.com/alussana/WebXiv.git
  cd WebXiv
  ./docker_build.sh
  ./docker_run.sh $VOLUME_DIR $INBOX_DIR $PORT
  ```

* WebXiv should now be reachable at `127.0.0.1:8080`

## Choose Credentials

Edit `conf/.htpassword` to set up your own credentials to access your files from the WWW.

## Restart WebXiv

* Stop WebXiv container with `Ctrl+C`.

* Remove all stopped Docker containers and old images.

  ```
  ./docker_clean.sh
  ```

* Start a new WebXiv instance.

  ```
  ./docker_build.sh
  ./docker_run.sh $VOLUME_DIR $INBOX_DIR $PORT
  ```