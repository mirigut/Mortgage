package math.utils;

import java.util.*;

public class PrimeUtils {
    public static boolean isPrime(long n) {
        if (n == 2) {
            return true;
        }
        for (long i = 2; i <= Math.ceil(Math.sqrt(n)) ; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static Set<Integer> findDivisors(int n) {
        Set<Integer> divisors = new HashSet<>();
        for (int i = 1; i <= Math.ceil(Math.sqrt(n)); i++) {
            if (n % i == 0) {
                divisors.add(i);
                divisors.add(n / i);
            }
        }
        return divisors;
    }

    public static List<Integer> sieve(int n) {
        n++;
        List<Boolean> allNumbers = new ArrayList<>(n);
        allNumbers.add(false);
        allNumbers.add(false);
        for (int i = 2; i < n; i++) {
            allNumbers.add(true);
        }
        for (int i = 2; i < n; i++) {
            if (allNumbers.get(i)) {
                for (int j = i * 2; j < n; j += i) {
                    allNumbers.set(j, false);
                }
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (allNumbers.get(i)) {
                primes.add(i);
            }
        }
        return primes;
    }
}
