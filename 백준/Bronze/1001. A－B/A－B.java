import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        //콘솔에서 입력받는 경우
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = 0;
        try {
            String[] strings = br.readLine().split(" ");

            int[] intArr = new int[strings.length];
            for(int i=0; i< intArr.length; i++) {
                intArr[i] = Integer.parseInt(strings[i]);
            }
            System.out.println(intArr[0]-intArr[1]);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }finally {
            br.close();
        }

    }
}