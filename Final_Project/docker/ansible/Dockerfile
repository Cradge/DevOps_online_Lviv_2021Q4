FROM ubuntu:20.04

RUN apt-get -y update && apt-get install -y python3 && apt-get install -y software-properties-common && add-apt-repository --yes --update ppa:ansible/ansible && apt-get install -y ansible

RUN mkdir /home/jenkins_home && mkdir /home/.ansible
