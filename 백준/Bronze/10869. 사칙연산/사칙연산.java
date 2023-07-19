import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            int result = 0;
            String[] strings = br.readLine().split(" ");
            int length = strings.length;

            int[] intArr = new int[length];

            for (int i = 0; i < length; i++) {
                intArr[i] = Integer.parseInt(strings[i]);
            }
            int first = intArr[0];
            int second = intArr[1];

            System.out.println(first + second);
            System.out.println(first - second);
            System.out.println(first * second);
            System.out.println(first / second);
            System.out.println(first % second);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}