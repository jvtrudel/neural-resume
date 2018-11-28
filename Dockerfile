FROM python:3-alpine3.7

RUN apk add --no-cache \
  # all this is needed for postgres' python driver
  python3-dev \
  gcc \
  musl-dev \ 
  postgresql-dev  \
  postgresql-client \
  # for graph_models (only needed in development environment)
  graphviz-dev  font-bitstream-type1\
  # front-end assets compilation
  nodejs

WORKDIR /app
COPY . /app


RUN npm install -g sass
RUN pip install -r requirements.txt
