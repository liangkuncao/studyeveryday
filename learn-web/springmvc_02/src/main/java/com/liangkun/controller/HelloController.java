package com.liangkun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HelloController {

    @RequestMapping(path="/hello")
    public String test1() {
        System.out.println("Hello Spring MVC!");
        return "success";
    }
}
