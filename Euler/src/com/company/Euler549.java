package com.company;

import math.utils.NumberFactors;
import math.utils.PrimeUtils;

import java.util.List;
import java.util.Map;

public class Euler549 {
    public static long solve() {
        int TOP = 100000000;
        List<Integer> sieve = PrimeUtils.sieve(TOP);
        long s = 0;
        for (int i = 2; i <= TOP  ; i++) {
            if (i % 100000 == 0) {
                System.out.println(i + "(" + i*100.0/TOP + ")");
            }
            NumberFactors factors = new NumberFactors(i, sieve);
            factors.setFactorialNeeded();
            long n = calcNumFromFacts(factors.getPrimeFactors());
            //System.out.println(i + " = " + printFacts(factors.getPrimeFactors()) + "  -  " + factors.getFactorialNeeded());
            s += (long)factors.getFactorialNeeded();

            if (i != n) {
                System.out.println(i + " FUCK");
            }
        }
        return s;

    }



    private static long calcNumFromFacts(Map<Integer, Integer> facts) {
        long n = 1;
        for (Map.Entry<Integer, Integer> entry : facts.entrySet()) {
            n = (long) (n * Math.pow(entry.getKey(), entry.getValue()));
        }
        return n;
    }

    private static String printFacts(Map<Integer, Integer> facts) {
        long n = 1;
        String s = "";
        for (Map.Entry<Integer, Integer> entry : facts.entrySet()) {
            for (int i = 0; i < entry.getValue(); i++) {
                s += entry.getKey() + " * ";
            }
        }
        s = s.substring(0,s.length() - 2);
        return s;
    }


}
