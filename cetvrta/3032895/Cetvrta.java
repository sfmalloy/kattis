import java.util.Scanner;

public class Cetvrta {

	public static void main(String[] args) {
		int[][] points = getPoints();
		int[] xValues = {points[0][0], points[1][0], points[2][0]};
		int[] yValues = {points[0][1], points[1][1], points[2][1]};
		System.out.println(getUnused(xValues) + " " + getUnused(yValues));
	}
	
	public static int[][] getPoints() {
		int[][] points = new int[4][2];
		
		Scanner scan = new Scanner(System.in);
		
		for(int i = 0; i < 3; ++i) {
			int x = scan.nextInt();
			int y = scan.nextInt();
			
			points[i][0] = x;
			points[i][1] = y;
		}
		
		return points;
	}
	
	public static int getUnused(int[] values) {
		
		if(values[0] == values[1]) {
			return values[2];
		} else if(values[1] == values[2]) {
			return values[0];
		} else {
			return values[1];
		}
	}

}
