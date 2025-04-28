package com.devops.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import javax.servlet.http.HttpServletRequest;

@RestController
public class HomeController {

    @GetMapping("/")
    public String getHomePage(HttpServletRequest request) {
        String baseUrl = getBaseUrl(request);
        
        return "<!DOCTYPE html>" +
                "<html lang='en'>" +
                "<head>" +
                "  <meta charset='UTF-8'>" +
                "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>" +
                "  <title>Welcome to DevOps</title>" +
                "  <link rel='stylesheet' href='/styles.css'>" +
                "</head>" +
                "<body>" +
                "  <div class='container'>" +
                "    <header>" +
                "      <h1>Welcome to the Ravi's DevOps Multi-Language Project</h1>" +
                "      <p>Showcasing Java, Python, and Go Microservices</p>" +
                "    </header>" +
                "    <section>" +
                "      <div class='links'>" +
                "        <a href='" + baseUrl + "/api/java' class='service-link'>Java Service</a>" +
                "        <a href='" + baseUrl + "/api/python' class='service-link'>Python Service</a>" +
                "        <a href='" + baseUrl + "/api/go' class='service-link'>Go Service</a>" +
                "      </div>" +
                "    </section>" +
                "    <footer>" +
                "      <p>&copy; 2025 DevOps Demo Project</p>" +
                "    </footer>" +
                "  </div>" +
                "</body>" +
                "</html>";
    }

    private String getBaseUrl(HttpServletRequest request) {
        return request.getScheme() + "://" + request.getServerName() + 
               (request.getServerPort() != 80 ? ":" + request.getServerPort() : "");
    }
}