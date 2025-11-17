FROM ubuntu:16.10

RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' \
           -e 's/security.ubuntu.com/old-releases.ubuntu.com/g' \
           /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client curl && \
    rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]