import java.util.Scanner;

public class TakeTwoStones {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int stones = scan.nextInt();
		
		if(stones % 2 == 0) {
			System.out.println("Bob");
		} else {
			System.out.println("Alice");
		}
	}

}
