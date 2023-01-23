FROM debian
WORKDIR /app
RUN apt update && apt install -y openjdk-17-jdk
COPY server.jar .
COPY eula.txt .
CMD java -jar server.jar