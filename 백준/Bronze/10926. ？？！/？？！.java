import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            String userId = br.readLine();
            System.out.println(userId + "??!");


        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}