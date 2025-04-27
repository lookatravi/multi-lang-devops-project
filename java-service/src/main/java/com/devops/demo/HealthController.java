package com.devops.demo;  // use your package name

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HealthController {

    @GetMapping("/api/java/health")
    public String health() {
        return "OK";
    }
}
