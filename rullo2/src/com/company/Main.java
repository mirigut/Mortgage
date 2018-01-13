package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        List<Integer> list = Arrays.asList(5,9,7,8,1,5,4,9);
        int sum = 41;


        Collections.sort(list);
        List<Integer> addands = new ArrayList<>();

        HashSet<List<Integer>> hs = (HashSet<List<Integer>>) rec(list, addands, sum);
        List<Integer> missing = new ArrayList<>(list);
        for (List<Integer> h : hs) {
            System.out.println(h);
            for (Integer i : h) {
                while (missing.contains(i)) {
                    missing.remove(i);
                }
            }
        }
        System.out.println("MISSING " + missing.toString());



    }

    public static Set<List<Integer>> rec(List<Integer> list, List<Integer> addands, int sum) {
        if (list.isEmpty()) {
            HashSet<List<Integer>> hs = new HashSet<>();
            int cur_sum = 0;
            for (Integer a : addands) {
                cur_sum += a.intValue();
            }
            if (cur_sum == sum) {
                hs.add(addands);
            }
            return hs;
        }

        Integer nextInt = list.get(0);

        List<Integer> newAddands = new ArrayList<>(addands);
        newAddands.add(nextInt);

        List<Integer> newList = removeFirst(list);
        HashSet<List<Integer>> hs = new HashSet<>();
        HashSet<List<Integer>> hs1 = (HashSet<List<Integer>>) rec(newList, addands, sum);
        HashSet<List<Integer>> hs2 = (HashSet<List<Integer>>) rec(newList, newAddands, sum);
        for (List<Integer> h : hs1) {
            hs.add(h);
        }
        for (List<Integer> h : hs2) {
            hs.add(h);
        }
        return hs;
    }

    public static List<Integer> removeFirst(List<Integer> list) {
        List<Integer> newList = new ArrayList<>();
        for (int i = 0; i < list.size() ; i++) {
            if (i > 0) {
                newList.add(list.get(i));
            }
        }
        return newList;

    }
}
