FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y openssh-client curl && \
    rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]