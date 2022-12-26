import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;


public class sol1 {
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
                    points = 1+3;
                    break;
                    case 'Y':
                    points = 2+6; 
                    break;
                    case 'Z':
                    points = 3+0; 
                    break;
                }
                break;
                case 'B':
                switch(p2){
                    case 'X':
                    points = 1+0;
                    break;
                    case 'Y':
                    points = 2+3; 
                    break;
                    case 'Z':
                    points = 3+6; 
                    break;
                }
                break;
                case 'C':
                switch(p2){
                    case 'X':
                    points = 1+6;
                    break;
                    case 'Y':
                    points = 2+0; 
                    break;
                    case 'Z':
                    points = 3+3; 
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