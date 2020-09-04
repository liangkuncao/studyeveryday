package com.liangkuncao.javacourse;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class ImmutableTest {
    @Test
    public void demonstrateImmutableString() {
        String s1 = "Hello";
        String s2 = "Hello";

        assertEquals(s1, s2);
        assertEquals("Hello", s1);

    }
}
