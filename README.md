# WebXiv

Personal NGINX web server and web archive running in a Docker container.

## Set up and start WebXiv

* Install [Docker](https://www.docker.com/)

* Install [htpasswd](https://httpd.apache.org/docs/2.4/programs/htpasswd.html)

* Choose a path that you want to be reachable from the WWW.

  ```
  VOLUME_DIR=/your/files/
  ```

* Choose a port where the server will be exposed on (replace `8080` with the desired port).

  ```
  PORT=8080
  ```

* Clone this repository.

  ```
  git clone https://github.com/alussana/WebXiv.git
  ```

* Create `conf/.htpassword` to set up your own credentials to access your files from the WWW. Replace `username` with your username.

  ```
  htpasswd -c WebXiv/conf/.htpasswd username
  ```

  You will be prompted to enter your password.


* Build and run the docker image.

  ```
  cd WebXiv
  ./docker_build.sh
  ./docker_run.sh $VOLUME_DIR $PORT
  ```

* WebXiv should now be reachable at `127.0.0.1:8080`

## Restart WebXiv

* Stop WebXiv container with `Ctrl+C`.

* Remove all stopped Docker containers and old images.

  ```
  ./docker_clean.sh
  ```

* Start a new WebXiv instance.

  ```
  ./docker_build.sh
  ./docker_run.sh $VOLUME_DIR $PORT
  ```