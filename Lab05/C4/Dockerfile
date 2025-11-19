FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y openssh-client openssh-server curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
RUN useradd -m -s /bin/bash prueba
RUN echo 'prueba:prueba' | chpasswd
RUN ssh-keygen -A

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]