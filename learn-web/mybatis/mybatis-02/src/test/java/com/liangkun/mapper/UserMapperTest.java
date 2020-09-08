package com.liangkun.mapper;

import com.liangkun.pojo.User;
import com.liangkun.util.MyBatisUtil;
import org.apache.ibatis.mapping.MappedStatement;
import org.apache.ibatis.session.SqlSession;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.sql.Statement;
import java.util.Collection;
import java.util.List;

public class UserMapperTest {
    SqlSession sqlSession;
    private UserMapper userMapper;

    @Before
    public void setUp() {
        sqlSession = MyBatisUtil.getSqlSession();
        userMapper = sqlSession.getMapper(UserMapper.class);

    }

    @After
    public void close() {
        sqlSession.close();
    }

    @Test
    public void selectUserList() {
        List<User> userList = userMapper.getUserList();

        for (User user : userList) {
            System.out.println(user);
        }
    }


    @Test
    public void getUserById() {
        User user = userMapper.getUserById(1);
        System.out.println(user);

    }

    @Test
    public void addUser() {
        User user = new User(3, "卢克", "123");
        int count = userMapper.addUser(user);
        sqlSession.commit();
        System.out.println(count);
    }

    @Test
    public void updateUser() {
        User user = new User(3, "卢克", "123456");
        int count = userMapper.updateUser(user);
        sqlSession.commit();
        System.out.println(count);
    }

    @Test
    public void deleteUserById() {
        int count = userMapper.deleteUserById(3);
        sqlSession.commit();
        System.out.println(count);
        for (User user : userMapper.getUserList()) {
            System.out.println(user);
        }
    }
}
