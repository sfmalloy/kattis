import java.util.Scanner;

public class FizzBuzz {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int x = scan.nextInt();
		int y = scan.nextInt();
		int n = scan.nextInt();
		
		for(int i = 1; i <= n; ++i) {
			if(i % x == 0) {
				System.out.print("Fizz");
			}
			
			if(i % y == 0) {
				System.out.print("Buzz");
			}
			
			if(i % x != 0 && i % y != 0) {
				System.out.print(i);
			}
			
			System.out.println();
		}
		
		scan.close();
	}

}
