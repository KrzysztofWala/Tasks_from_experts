FROM ubuntu:latest
ARG ARG_VAR
ENV MY_ENV=VALUE
RUN apt update
RUN apt install python3 -y
RUN useradd ${ARG_VAR}
USER ${ARG_VAR}
RUN echo "User ${ARG_VAR} was created"
WORKDIR /app_directory
COPY . .
CMD python3 /app_directory/app.py
