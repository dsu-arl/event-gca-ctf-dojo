FROM debian

RUN apt update; apt install firefox-esr python3 python3-pip python3-flask -y

RUN <<EOF
    useradd -s /bin/bash -m hacker
    passwd -d hacker
    ln -s /etc/bash.bashrc /etc/bashrc
EOF

ADD --chown=0:0 --chmod=6755 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

USER hacker
