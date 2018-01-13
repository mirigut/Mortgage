package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        long start = System.currentTimeMillis();

        System.out.println(Euler549.solve());

        long stop = System.currentTimeMillis();
        printTime(start, stop);
    }

    private static void printTime(long start, long stop) {
        double timeInSecs = (stop - start) / 1000.0;
        System.out.println("Took " + timeInSecs + " seconds");
    }

}
