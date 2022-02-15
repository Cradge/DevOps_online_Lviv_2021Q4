FROM openjdk:11-jre-slim

RUN mkdir /home/petclinic

COPY app.jar /home/petclinic/app.jar

CMD ["java","-jar","/home/petclinic/app.jar"]

EXPOSE 8080
