import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;


public class sol2 {
    public static void main(String[] args) throws IOException {
        FileInputStream fileByteStream = null;
        Scanner inFS = null;

        fileByteStream = new FileInputStream("input.txt");
        inFS = new Scanner(fileByteStream);

        char p1;
        char p2;
        String line = "";
        int points = 0;
        int tot = 0;
        while(inFS.hasNext()){
            line = inFS.nextLine();
            p1 = line.charAt(0);
            p2 = line.charAt(2);
            switch(p1){
                case 'A':
                switch(p2){
                    case 'X':
                    points = 0+3;
                    break;
                    case 'Y':
                    points = 3+1; 
                    break;
                    case 'Z':
                    points = 6+2; 
                    break;
                }
                break;
                case 'B':
                switch(p2){
                    case 'X':
                    points = 0+1;
                    break;
                    case 'Y':
                    points = 3+2; 
                    break;
                    case 'Z':
                    points = 6+3; 
                    break;
                }
                break;
                case 'C':
                switch(p2){
                    case 'X':
                    points = 0+2;
                    break;
                    case 'Y':
                    points = 3+3; 
                    break;
                    case 'Z':
                    points = 6+1; 
                    break;
                }
                break;
            }
            tot += points;
        }
        inFS.close();
        System.out.println(tot);
    }
}