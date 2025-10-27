package com.javamicroservice.UserDirectoryJavaBackend;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface LocalAuthRepo extends JpaRepository<AuthUser, Integer> {
    Optional<AuthUser> findByEmail(String email);
}
