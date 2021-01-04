package com.liangkuncao.javacourse;

import org.junit.Test;

import static org.junit.Assert.*;

public class PorscheTest {

    @Test
    public void shouldCloneStringArray() {
        String[] array = {"one", "two", "three"};
        String[] copiedArray = array.clone();
        assertNotSame(array, copiedArray);
        assertSame(array, array);

        for (String str : array) {
            System.out.println(str);
        }
        System.out.println(array.length);
    }
    @Test
    public void shouldClonePorsche() {
        Porsche marcusPorsche = new Porsche("Marcus");
        Porsche peterPorsche = marcusPorsche.clone();

        assertNotSame(marcusPorsche, peterPorsche);
        assertEquals(marcusPorsche.asString(), peterPorsche.asString());
        System.out.println(peterPorsche.asString());
    }
}
