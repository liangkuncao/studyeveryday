package com.liangkuncao.javacourse;

import org.junit.Test;

import javax.xml.bind.DatatypeConverter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.assertEquals;

public class Md5Test {
    @Test
    public void givenPassword_whenHashing_thenVerifying() throws NoSuchAlgorithmException {
        String hash = "35454B055CC325EA1AF2126E27707052";
        String password = "ILoveJava";

        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(password.getBytes());
        byte[] digest = md.digest();
        String myHash = DatatypeConverter.printHexBinary(digest).toUpperCase();
//        System.out.println(myHash);
        assertEquals(myHash, hash);
    }

    @Test
    public void givenFile_generatingChecksum_thenVerifying() throws NoSuchAlgorithmException, IOException {
        String filename = "src/test/resources/test_md5.txt";
        String checksum = "35454B055CC325EA1AF2126E27707052";

        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(Files.readAllBytes(Paths.get(filename)));
        byte[] digest = md.digest();
        String myChecksum = DatatypeConverter.printHexBinary(digest).toUpperCase();
        assertEquals(checksum, myChecksum);
    }
}
