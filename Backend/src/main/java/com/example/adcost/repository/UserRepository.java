package com.example.adcost.repository;

import com.example.adcost.model.User;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserRepository extends MongoRepository<User, ObjectId> {
    List<User> findAll();
    List<User> findAllByUid(String uid);
    void deleteByUid(String uid);
}
