import java.util.Scanner;

public class PrintedStatues {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int printerCount = 1;
        int statueCount = 0;
        int daysPassed = 0;
        
        int statuesNeeded = scan.nextInt();
        
        while(printerCount < statuesNeeded / 2) {
            printerCount *= 2;
            ++daysPassed;
        }
        
        while(statueCount < statuesNeeded) {
            statueCount += printerCount;
            ++daysPassed;
        }
        
        scan.close();
        System.out.println(daysPassed);
    }

}