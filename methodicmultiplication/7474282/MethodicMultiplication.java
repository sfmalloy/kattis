/*
RULES
-----
x + 0 = x
x * 0 = 0
x + S(y) = S(x + y)
x * S(y) = x * y + x
 */

import java.util.Scanner;
import java.util.List;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toList;

public class MethodicMultiplication {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long xCount = sCount(scan.nextLine());
        long yCount = sCount(scan.nextLine());
        StringBuilder begin = new StringBuilder();
        StringBuilder end = new StringBuilder();
        end.append("0");
        for (int i = 0; i < xCount * yCount; ++i) {
            begin.append("S(");
            end.append(")");
        }

        System.out.println(begin.toString() + end.toString());
    }

    public static long sCount(String line) {
        return line.chars().filter(chr -> chr == 'S').count();
    }
}
