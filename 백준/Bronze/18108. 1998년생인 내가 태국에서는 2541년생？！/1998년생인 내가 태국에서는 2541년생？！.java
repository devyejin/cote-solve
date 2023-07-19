import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 불기 = 서기 + 544
 */
public class Main {
    public static void main(String[] args) {

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            int buddhismYear = Integer.parseInt(br.readLine());

            int adYear = buddToAd(buddhismYear);
            System.out.println(adYear);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    private static int buddToAd(int buddhismYear) {
        return buddhismYear - 544 + 1;
    }
}