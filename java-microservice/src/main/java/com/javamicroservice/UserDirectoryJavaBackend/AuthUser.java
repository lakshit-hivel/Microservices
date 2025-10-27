package com.javamicroservice.UserDirectoryJavaBackend;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "\"authUser\"")
public class AuthUser {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String email;
    private String password;
    private String username;
}
