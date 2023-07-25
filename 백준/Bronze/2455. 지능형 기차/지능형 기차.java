import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {


        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {

            int[] status = new int[4];
            int length = status.length;

            String[][] onOff = new String[4][2];

            //입력받기
            for (int i = 0; i < length; i++) {
                onOff[i] = br.readLine().split(" ");
            }

            for (int i = 0; i < length; i++) {
                int temp = -Integer.parseInt(onOff[i][0]) + Integer.parseInt(onOff[i][1]);

                if (i > 0) status[i] += status[i - 1] + temp;
                else status[i] += temp;

            }

            System.out.println(Arrays.stream(status).max().getAsInt());


        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}