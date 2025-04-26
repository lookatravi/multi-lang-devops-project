FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/java-service-1.0.0.jar /app/java-service.jar
EXPOSE 8080
CMD ["java", "-jar", "/app/java-service.jar"]
