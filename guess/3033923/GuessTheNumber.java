import java.util.Scanner;

public class GuessTheNumber {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int min = 1;
		int max = 1000;
		
		for (int i = 0; i < 10; ++i) {
			int guess = (max + min) / 2;
			
			System.out.println(guess);
			
			String response = scan.nextLine();
			
			if (response.equals("lower")) {
				max = guess - 1;
			} else if (response.equals("higher")) {
				min = guess + 1;
			} else {
				break;
			}
		}
		
		scan.close();
	}
	
}
