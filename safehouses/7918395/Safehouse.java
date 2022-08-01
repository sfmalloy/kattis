import java.util.Scanner;
import java.util.ArrayList;

public class Safehouse {
    public static class Point {
        public int x;
        public int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        ArrayList<Point> safehouses = new ArrayList<>();
        ArrayList<Point> spies = new ArrayList<>();

        for (int r = 0; r < N; ++r) {
            String line = scan.next();
            for (int c = 0; c < N; ++c) {
                if (line.charAt(c) == 'H') {
                    safehouses.add(new Point(r, c));
                } else if (line.charAt(c) == 'S') {
                    spies.add(new Point(r, c));
                }
            }
        }

        scan.close();

        int maxDist = spies.stream().map((s) -> safehouses.stream().map((h) -> dist(s, h)).min(Integer::compare).get()).max(Integer::compare).get();
        System.out.println(maxDist);
    }

    public static int dist(Point a, Point b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }
}
