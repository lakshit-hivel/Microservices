package com.javamicroservice.UserDirectoryJavaBackend;

import org.springframework.web.bind.annotation.*;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import java.time.LocalDateTime;

interface UserRepo extends JpaRepository<User, Integer> {
    List<User> findByIsDeleted(Boolean isDeleted);
}

class UserResponse {
    private List<User> data;
    private String message;

    public UserResponse(String message, List<User> data) {
        this.data = data;
        this.message = message;
    }

    public List<User> getData() {
        return data;
    }

    public String getMessage() {
        return message;
    }
}

@RestController
@RequestMapping("/api/")
public class UserController {

    @Autowired
    private UserRepo repo;

    @GetMapping("/all-users")
    public UserResponse getAll(@RequestParam(required = false, defaultValue = "false") Boolean isDeleted) {
        return new UserResponse("All users fetched successfully", repo.findByIsDeleted(isDeleted));
    }

    @PostMapping("/new-user")
    public User create(@RequestBody User user) {
        return repo.save(user);
    }

    @GetMapping("/get-user/{id}")
    public User getOne(@PathVariable Integer id) {
        return repo.findById(id).orElse(null);
    }

    @PutMapping("/update-user/{id}")
    public User update(@PathVariable Integer id, @RequestBody User user) {
        return repo.findById(id).map(u -> {
            u.setName(user.getName());
            u.setEmail(user.getEmail());
            u.setAge(user.getAge());
            u.setUniversity(user.getUniversity());
            u.setCompany(user.getCompany());
            u.setTitle(user.getTitle());
            u.setDepartment(user.getDepartment());
            u.setAddress(user.getAddress());
            u.setState(user.getState());
            u.setCity(user.getCity());
            u.setPhone(user.getPhone());
            u.setCountry(user.getCountry());
            u.setGender(user.getGender());
            u.setProfilePicture(user.getProfilePicture());
            u.setRole(user.getRole());
            u.setIsDeleted(user.getIsDeleted());
            u.setDeletedAt(user.getDeletedAt());
            u.setCreatedAt(user.getCreatedAt());
            u.setUpdatedAt(user.getUpdatedAt());
            return repo.save(u);
        }).orElse(null);
    }

    @DeleteMapping("/delete-user/{id}")
    public void delete(@PathVariable Integer id) {
        repo.findById(id).map(u -> {
            u.setIsDeleted(true);
            u.setDeletedAt(LocalDateTime.now());
            return repo.save(u);
        }).orElse(null);
    }

    @PutMapping("/restore-user/{id}")
    public User restore(@PathVariable Integer id) {
        return repo.findById(id).map(u -> {
            u.setIsDeleted(false);
            return repo.save(u);
        }).orElse(null);
    }

    @GetMapping("/all-deleted-users")
    public UserResponse getAllDeletedUsers() {
        return new UserResponse("All deleted users fetched successfully", repo.findByIsDeleted(true));
    }
}
