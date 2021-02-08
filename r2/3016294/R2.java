import java.util.Scanner;

public class R2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int r1 = scan.nextInt();
		int s = scan.nextInt();
		
		int r2 = 2 * s - r1;
		System.out.println(r2);
	}

}
