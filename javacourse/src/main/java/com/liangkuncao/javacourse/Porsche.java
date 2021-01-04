package com.liangkuncao.javacourse;

public class Porsche implements Cloneable {
    private String owner;

    public Porsche(String owner) {
        this.owner = owner;
    }

    @Override
    public Porsche clone() {
        try {
            return (Porsche) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }

    public String asString() {
        return "Car: " + this.owner;
    }
}
