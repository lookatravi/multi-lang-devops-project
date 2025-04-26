package com.devops.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class JavaServiceController {

    @GetMapping("/api/java")
    public String getJavaService() {
        return "<!DOCTYPE html>" +
                "<html lang='en'>" +
                "<head>" +
                "  <meta charset='UTF-8'>" +
                "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>" +
                "  <title>Java Service</title>" +
                "  <link rel='stylesheet' href='/styles.css'>" +
                "</head>" +
                "<body class='java-page'>" +
                "  <div class='container'>" +
                "    <header>" +
                "      <h1>Welcome to the Java Microservice</h1>" +
                "      <p>This is the Java service endpoint powered by Spring Boot</p>" +
                "    </header>" +
                "    <section>" +
                "      <div class='links'>" +
                "        <a href='/' class='service-link'>Back to Home</a>" +
                "      </div>" +
                "    </section>" +
                "    <footer>" +
                "      <p>&copy; 2025 DevOps Demo Project</p>" +
                "    </footer>" +
                "  </div>" +
                "</body>" +
                "</html>";
    }
}
