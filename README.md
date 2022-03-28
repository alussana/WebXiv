# WebXiv

Personal NGINX web server and web archive running in a Docker container.

## Set up and start WebXiv

* Install [Docker](https://www.docker.com/)

* Choose a path that you want to be reachable from the WWW.

  ```
  VOLUME_DIR=/your/files/
  ```

* Choose a path where to create inbox.txt; messages coming from the website will be stored here.

  ```
  INBOX_DIR=/your/files/inbox/
  ```

* Choose a port where the server will be exposed on (replace `8080` with the desired port).

  ```
  $PORT=8080
  ```

* Clone this repository.

  ```
  git clone https://github.com/alussana/WebXiv.git
  ```

* Create `conf/.htpassword` to set up your own credentials to access your files from the WWW. Replace `username` and `password` with your username and password.

  ```
  echo "username:password" > WebXiv/conf/.htpasswd
  ```

* Create `telegram_bot/.env` to store the API token used by the WebXiv Telegram bot, and an authorized Telegram user ID. If you don't have a token, talk with the [Botfather](https://telegram.me/botfather) to get one. If you don't know your user ID, talk with the [Json Dump Bot](https://t.me/jsondumpbot) to retrieve it.

  ```
  echo 'TOKEN="yourToken"' > WebXiv/telegram_bot/.env
  echo 'AUTHORIZED_USER="yourId"' >>  WebXiv/telegram_bot/.env
  ```

* Build and run the docker image.

  ```
  cd WebXiv
  ./docker_build.sh
  ./docker_run.sh $VOLUME_DIR $INBOX_DIR $PORT
  ```

* WebXiv should now be reachable at `127.0.0.1:8080`

* Start a conversation on [Telegram](https://telegram.org/) with the `webXiv_bot` to receive notifications of incoming messages.

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