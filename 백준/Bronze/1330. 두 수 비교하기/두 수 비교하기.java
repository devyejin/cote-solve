import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {


        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {

            StringTokenizer tokenizer = new StringTokenizer(br.readLine());

            if(tokenizer.hasMoreTokens()) {
                int A = Integer.parseInt(tokenizer.nextToken());
                int B = Integer.parseInt(tokenizer.nextToken());

                String result = (A > B) ? ">" :  (A < B) ? "<" : "==";

                System.out.println(result);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}