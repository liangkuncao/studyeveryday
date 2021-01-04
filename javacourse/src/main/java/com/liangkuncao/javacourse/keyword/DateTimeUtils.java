package com.liangkuncao.javacourse.keyword;

public class DateTimeUtils {
    public native String getSystemTime();

    static {
        System.loadLibrary("nativedatetimeutils");
    }
}
