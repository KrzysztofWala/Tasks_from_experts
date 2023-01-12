FROM ubuntu:latest
ARG ARG_VAR
ENV MY_ENV=VALUE
ENV MY_ENV1=${FROM_FILE1}
ENV MY_ENV2=${FROM_FILE2}
ENV MY_ENV3=${FROM_FILE3}
RUN apt update
RUN apt install python3 -y
RUN useradd ${ARG_VAR}
USER ${ARG_VAR}
RUN echo "User ${ARG_VAR} was created"
WORKDIR /app_directory
COPY . .
CMD python3 /app_directory/app.py
