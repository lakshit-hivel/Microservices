package com.javamicroservice.UserDirectoryJavaBackend;

import org.springframework.web.bind.annotation.*;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;

interface UserRepo extends JpaRepository<User, Integer> {
}

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserRepo repo;

    @GetMapping
    public List<User> getAll() {
        return repo.findAll();
    }

    @PostMapping
    public User create(@RequestBody User user) {
        return repo.save(user);
    }

    @GetMapping("/{id}")
    public User getOne(@PathVariable Integer id) {
        return repo.findById(id).orElse(null);
    }

    @PutMapping("/{id}")
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

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Integer id) {
        repo.deleteById(id);
    }
}
