# gpt-proxy-server

### Deploy

0. clone this repo

```bash
git clone https://github.com/devnjw/gpt-proxy-server.git
cd gpt-proxy-server
```

1. create a `.env` file with the following variables:

```bash
OPENAI_API_KEY=<your openai api key>
```

2. build and run the docker container

```bash
docker build -t gpt-proxy-server .
docker run -it --rm --env-file .env -p 8080:8080 gpt-proxy-server
```
