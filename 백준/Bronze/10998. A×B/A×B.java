
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        //콘솔에서 입력받는 경우

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            int result = 0;
            String[] strings = br.readLine().split(" ");
            int length = strings.length;

            int[] intArr = new int[length];

            for (int i = 0; i < length; i++) {
                intArr[i] = Integer.parseInt(strings[i]);
            }

            System.out.println(intArr[0] * intArr[1]);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}