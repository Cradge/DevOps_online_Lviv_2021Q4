FROM ubuntu:20.04

RUN apt-get -y update && apt-get install -y curl && apt-get install -y gnupg && apt-get install -y lsb-release && apt-get install -y software-properties-common && apt-get install -y unzip

RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && apt-get -y update && apt-get install -y terraform

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install

RUN mkdir /home/jenkins_home
