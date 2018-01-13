package com.company;

public class Euler145 {
    public static long solve() {
        int c = 0;
        int top = 1000000000;
        for (int i = 0; i < top ; i++) {
            if (i % 1000000 == 0) {
                System.out.println(i*1.0/top);
            }
            if (isReversible(i)) {
                c += 1;
            }
        }
        System.out.println("----------------");
        System.out.println(c);
        return 0;
    }

    private static boolean isReversible(int n) {
        if (n % 10 == 0) {
            return false;
        }
        return isAllOdd(n + reverse(n));

    }

    private static boolean isAllOdd(int n) {
        while (n > 1) {
            if (n % 2 == 0) {
                return false;
            }
            n = n/10;
        }
        return true;
    }

    private static int reverse(int n) {
        int rev = 0;

        while (n >= 1) {
            rev = rev * 10 + n%10;
            n = n / 10;

        }

        return rev;
    }
}
