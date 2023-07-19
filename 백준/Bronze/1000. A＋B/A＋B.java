
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

            for(String s : strings) {
                sum += Integer.parseInt(s);
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }finally {
            br.close();
        }

        System.out.println(sum);
    }
}