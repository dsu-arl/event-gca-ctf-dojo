FROM ubuntu

USER root

RUN <<EOF
	if id ubuntu; then userdel -f -r ubuntu; fi
	useradd -s /bin/bash -m hacker
	passwd -d hacker

	ln -s /etc/bash.bashrc /etc/bashrc
EOF

RUN <<EOF
	apt update && apt install git binutils python3.12 -y
	# apt install python3.12 -y
EOF

ADD --chown=0:0 --chmod=6755 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
# RUN chmod 6755 /usr/bin/exec-suid
COPY ./string-analysis/locateTheString /home/hacker/locateTheString_Challenge01