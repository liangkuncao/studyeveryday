package com.liangkuncao.javacourse.keyword;

import org.junit.BeforeClass;
import org.junit.Test;

public class DateTimeUtilsTest {
    @BeforeClass
    public static void setUpClass() {
        System.loadLibrary("nativedatetimeutils");
    }
    @Test
    public void givenNativeLibsLoaded_thenNativeMethodIsAccessible() {
        DateTimeUtils dateTimeUtils = new DateTimeUtils();
        System.out.println("System time is: " + dateTimeUtils.getSystemTime());

    }
}
