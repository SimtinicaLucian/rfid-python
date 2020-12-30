package com.example.adcost.resource;

import com.example.adcost.model.User;
import com.example.adcost.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/api")
@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
@RequiredArgsConstructor
public class UserController {
    public final UserService userService;

    @GetMapping("/view")
    public List<User> viewAllUsers(){
        return userService.getAllUsers();
    }

    @PostMapping(value = "/add")
    public User persist(@RequestBody User user) {
        return userService.saveUser(user);
    }
    @DeleteMapping(value = "/delete/{uid}")
    public void deleteUid(@PathVariable String uid) {
        userService.deleteUid(uid);
    }
}
