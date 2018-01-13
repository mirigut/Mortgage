package math.utils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NumberFactors {
    int number;
    Map<Integer, Integer> primeFactors;
    int maxFactor = 0;

    int maxFactorCount;

    int factorialNeeded = 0;

    public NumberFactors(int number, List<Integer> sieve) {
        this.number = number;

        primeFactors = new HashMap<>(findPrimeFactors(number, sieve));
        for (Map.Entry<Integer, Integer> entry : primeFactors.entrySet()) {
            if (entry.getKey() > maxFactor) {
                maxFactor = entry.getKey();
                maxFactorCount = entry.getValue();
            }
        }
    }

    public static Map<Integer,Integer> findPrimeFactors(int n, List<Integer> sieve) {
        Map<Integer,Integer> primeFactors = new HashMap<>();
        while (n > 1) {
            for (Integer p : sieve) {
                if (p > Math.sqrt(n)) {
                    int currentCount = primeFactors.containsKey(n) ? primeFactors.get(n) : 0;
                    primeFactors.put((int) n, currentCount + 1);
                    n = n / n;
                    break;
                }
                if (n % p == 0) {
                    int currentCount = primeFactors.containsKey(p) ? primeFactors.get(p) : 0;
                    primeFactors.put(p, currentCount + 1);
                    n = n / p;
                    break;
                }
            }
        }
        return primeFactors;
    }

    public void setFactorialNeeded() {
        if (number == 12) {
            int b = 30;
        }
    /*    if (maxFactorCount == 1) {
            factorialNeeded = maxFactor;
            return;
        }*/

        int maxSingleFact = 0;
        for (Map.Entry<Integer, Integer> entry : primeFactors.entrySet()) {
            int singleFact = findSingleFact(entry.getKey(), entry.getValue());
            if (singleFact > maxSingleFact) {
                maxSingleFact = singleFact;
            }
        }
        factorialNeeded = maxSingleFact;

    }

    private int howManyMults(int n, int div) {
        int count = 0;
        while (n % div == 0) {
            n = n / div;
            count++;
        }
        return count;
    }

    private int findSingleFact(int n, int times) {
        int count = 0;
        int i = 0;
        while (count < times) {
            i++;
            count += howManyMults(i*n, n);
        }
        return i*n;
    }

    public int getFactorialNeeded() {
        return factorialNeeded;
    }

    public int getNumber() {
        return number;
    }

    public Map<Integer, Integer> getPrimeFactors() {
        return primeFactors;
    }

    public int getMaxFactor() {
        return maxFactor;
    }

    public int getMaxFactorCount() {
        return maxFactorCount;
    }


}