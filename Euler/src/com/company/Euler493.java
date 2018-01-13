package com.company;

public class Euler493 {

  /*
    E[X] = E[X_1] + E[X_2] + ... + E[X_7] = 7*E[X_1] = 7 * Pr(color A exists) = 7 * (1 - Pr(Color A doesn't exist))

    Pr(Color A doesn't exist) = (60/70) * (59/69) * (58/68) * ... * (41/51)
    */

    public static double solve() {
        double frac = calcFrac(70,20);
        return 7 * (1.0 - frac);
    }

    private static double calcFrac(int n, int k) {
        double res = 1.0;
        for (int i = 0; i < k; i++) {
            res = res * ((n-10-i)*1.0)/(n-i);
        }
        return res;
    }


}
