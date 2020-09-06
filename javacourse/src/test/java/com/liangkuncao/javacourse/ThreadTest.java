package com.liangkuncao.javacourse;

import org.junit.Test;

public class ThreadTest {
    @Test
    public void testThread() {
        Thread thread1 = new Thread(new MyThread());
        thread1.start();

    }
}
