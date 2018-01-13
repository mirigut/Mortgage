package com.company;

import math.utils.PrimeUtils;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Euler387 {
    public static long solve() {
        Map<Long, Set<Long>> nums = new HashMap<>();
        Set<Long> s0 = new HashSet<>();
        Set<Long> goal = new HashSet<>();
        for (long i = 1; i < 10; i++) {
            s0.add(i);
        }
        nums.put((long) 1, s0);
        for (long i = 2; i < 15; i++) {
            Set<Long> s = new HashSet<>();
            Set<Long> prev_s = nums.get(i - 1);

            for(Long p : prev_s) {
                boolean isPStrongHarshad = PrimeUtils.isPrime(p / sumDigits(p));
                for (long last_dig = 0; last_dig < 10 ; last_dig++) {
                    Long new_p = p*10 + last_dig;
                    if (isHarshad(new_p)) {
                        s.add(new_p);
                    }
                    if (new_p >= 100 && isPStrongHarshad && PrimeUtils.isPrime(new_p)) {
                        goal.add(new_p);
                    }
                }
            }
            nums.put(i, s);
        }
        long res = 0;
        for (Long g: goal) {
            res += g;
        }
        return res;
    }

    private static long sumDigits(long n) {
        long s = 0;
        while (n > 0) {
           s += n % 10;
           n = n / 10;
        }
        return s;
    }

    private static boolean isHarshad(long n) {
        return n % sumDigits(n) == 0;
    }

}
