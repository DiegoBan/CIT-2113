FROM ubuntu:22.10

RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' \
           -e 's/security.ubuntu.com/old-releases.ubuntu.com/g' \
           /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y openssh-client openssh-server curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/bash prueba

RUN echo 'prueba:prueba' | chpasswd

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM no/UsePAM yes/' /etc/ssh/sshd_config

RUN ssh-keygen -A

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]