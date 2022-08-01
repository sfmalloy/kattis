import java.util.HashSet;
import java.util.Scanner;

public class MagicTrick {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        HashSet<Character> letters = new HashSet<Character>();

        String word = input.nextLine();
        for (int i = 0; i < word.length(); ++i) {
            letters.add(word.charAt(i));
        }

        System.out.println(letters.size() == word.length() ? 1 : 0);
    }
}
