FROM maven:3.8.6-amazoncorretto-17 as builder
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN mvn clean package

FROM amazoncorretto:17
WORKDIR /app
COPY --from=builder /build/target/*.jar app.jar
COPY src/main/resources/static ./static/
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]