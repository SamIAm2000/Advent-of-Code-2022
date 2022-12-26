import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;


public class sol {
    public static void main(String[] args) throws IOException {
        FileInputStream fileByteStream = null;
        Scanner inFS = null;

        fileByteStream = new FileInputStream("input.txt");
        inFS = new Scanner(fileByteStream);
        ArrayList<Integer> intArr = new ArrayList<Integer>();
        int max = 0;
        int cur = 0;
        int curSum = 0;
        String str = "";

        while (inFS.hasNext()) {
            str = inFS.nextLine();
            if (!str.isEmpty()){
                cur = Integer.valueOf(str);
                curSum += cur;
            } else {
                intArr.add(curSum);
                curSum = 0;
            }
        }
        Collections.sort(intArr);
        max +=intArr.get(intArr.size() -1);
        max +=intArr.get(intArr.size() -2);
        max +=intArr.get(intArr.size() -3);
        fileByteStream.close();
        inFS.close();
        System.out.println(max);

    }
}