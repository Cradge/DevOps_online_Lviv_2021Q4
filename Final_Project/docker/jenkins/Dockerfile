FROM jenkins/jenkins:lts-jdk11

RUN mkdir /var/jenkins_home/.ssh && ssh-keygen -t ed25519 -a 100 -f /var/jenkins_home/.ssh/ed25519 -q -N "" && mkdir /var/jenkins_home/.provision && ssh-keygen -t ed25519 -a 100 -f /var/jenkins_home/.provision/private -q -N ""

USER root

RUN apt-get update && apt-get install -y sudo && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN curl -sSL https://get.docker.com/ | sh

RUN apt-get install -y npm && npm install -y --global smee-client

USER jenkins
