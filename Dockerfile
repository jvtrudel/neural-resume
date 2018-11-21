FROM python:3-alpine3.7

RUN apk add --no-cache \
  gcc \
  python3-dev \
  musl-dev \
  postgresql-dev  \
  postgresql-client \
  graphviz-dev  font-bitstream-type1

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
