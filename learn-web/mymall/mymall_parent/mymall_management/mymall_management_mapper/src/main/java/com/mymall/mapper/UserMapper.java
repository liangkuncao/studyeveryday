package com.liangkun.mapper;

import com.liangkun.pojo.User;

import java.util.List;

public interface UserMapper {
    List<User> getUserList();

    User getUserById(int id);

    int addUser(User user);

    int updateUser(User user);

    int deleteUserById(int id);
}
