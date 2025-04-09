FROM ubuntu

RUN <<EOF
	apt update && apt install git binutils -y
EOF

ADD --chown=0:0 --chmod=6755 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
COPY ./string-analysis/locateTheString /home/ubuntu/locateTheString_Challenge01