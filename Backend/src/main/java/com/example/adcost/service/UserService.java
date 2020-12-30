package com.example.adcost.service;

import com.example.adcost.model.User;
import com.example.adcost.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;


    public List<User> getAllUsers() {
        return userRepository.findAll();
    }


    public User saveUser(User user) {
        List<User> userSearch = userRepository.findAllByUid(user.getUid());
        if (userSearch.size() < 1) {
            user = userRepository.save(user);
        }
        return user;
    }

    public void deleteUid(String uid) {
        userRepository.deleteByUid(uid);
    }


}
