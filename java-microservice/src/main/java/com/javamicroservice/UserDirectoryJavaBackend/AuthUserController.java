package com.javamicroservice.UserDirectoryJavaBackend;

import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import javax.crypto.SecretKey;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.*;

class AuthResponse {
    private String message;
    private String token;

    public AuthResponse(String message, String token) {
        this.message = message;
        this.token = token;
    }

    public AuthResponse(String message) {
        this.message = message;
        this.token = null;
    }

    public String getMessage() {
        return message;
    }

    public String getToken() {
        return token;
    }
}

@RestController
@RequestMapping("/auth")
public class AuthUserController {

    private static final Logger logger = LoggerFactory.getLogger(AuthUserController.class);

    @Autowired
    private LocalAuthRepo localAuthRepo;

    private final String jwtSecretString = "mySecretJwtKeyForHS256AlgorithmMustBe256BitsLong";
    private final SecretKey jwtSecret = Keys.hmacShaKeyFor(jwtSecretString.getBytes());

    @PostMapping("/register")
    public ResponseEntity<AuthResponse> register(@RequestBody AuthUser user) {
        logger.info("Registration attempt for email: {}", user.getEmail());

        if (localAuthRepo.findByEmail(user.getEmail()).isPresent()) {
            logger.warn("Registration failed - Email already exists: {}", user.getEmail());
            return ResponseEntity.badRequest()
                    .body(new AuthResponse("Email already exists"));
        }

        String token = Jwts.builder()
                .setSubject(user.getEmail())
                .setExpiration(new Date(System.currentTimeMillis() + 86400000))
                .signWith(jwtSecret)
                .compact();

        localAuthRepo.save(user);
        logger.info("User registered successfully: {}", user.getEmail());
        return ResponseEntity.ok(new AuthResponse("User registered successfully", token));
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody AuthUser user) {
        logger.info("Login attempt for email: {}", user.getEmail());

        Optional<AuthUser> found = localAuthRepo.findByEmail(user.getEmail());

        if (found.isEmpty() || !user.getPassword().equals(found.get().getPassword())) {
            logger.warn("Login failed - Invalid credentials for email: {}", user.getEmail());
            return ResponseEntity.badRequest()
                    .body(new AuthResponse("Invalid credentials"));
        }

        String token = Jwts.builder()
                .setSubject(found.get().getEmail())
                .setExpiration(new Date(System.currentTimeMillis() + 86400000))
                .signWith(jwtSecret)
                .compact();

        logger.info("Login successful for email: {}", user.getEmail());
        return ResponseEntity.ok(new AuthResponse("Login successful", token));
    }
}
