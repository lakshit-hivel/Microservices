package com.javamicroservice.UserDirectoryJavaBackend;

import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.*;

@RestController
@RequestMapping("/auth")
public class AuthUserController {

    private static final Logger logger = LoggerFactory.getLogger(AuthUserController.class);

    @Autowired
    private LocalAuthRepo localAuthRepo;

    private final String jwtSecret = "mySecretJwtKeyForHS256AlgorithmMustBe256BitsLong";

    @PostMapping("/register")
    public Map<String, String> register(@RequestBody AuthUser user) {
        logger.info("Registration attempt for email: {}", user.getEmail());

        if (localAuthRepo.findByEmail(user.getEmail()).isPresent()) {
            logger.warn("Registration failed - Email already exists: {}", user.getEmail());
            return Map.of("message", "Email already exists");
        }

        String token = Jwts.builder()
                .setSubject(user.getEmail())
                .setExpiration(new Date(System.currentTimeMillis() + 86400000))
                .signWith(SignatureAlgorithm.HS256, jwtSecret)
                .compact();

        localAuthRepo.save(user);
        logger.info("User registered successfully: {}", user.getEmail());
        return Map.of("message", "User registered successfully", "token", token);
    }

    @PostMapping("/login")
    public Map<String, String> login(@RequestBody AuthUser user) {
        logger.info("Login attempt for email: {}", user.getEmail());

        Optional<AuthUser> found = localAuthRepo.findByEmail(user.getEmail());

        if (found.isEmpty() || !user.getPassword().equals(found.get().getPassword())) {
            logger.warn("Login failed - Invalid credentials for email: {}", user.getEmail());
            return Map.of("message", "Invalid credentials");
        }

        String token = Jwts.builder()
                .setSubject(found.get().getEmail())
                .setExpiration(new Date(System.currentTimeMillis() + 86400000))
                .signWith(SignatureAlgorithm.HS256, jwtSecret)
                .compact();

        logger.info("Login successful for email: {}", user.getEmail());
        return Map.of("message", "Login successful", "token", token);
    }
}
