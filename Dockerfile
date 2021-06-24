FROM ubuntu:20.04

RUN apt update && apt upgrade -y
RUN apt install -y lame sox ffmpeg

CMD tail -f /dev/null