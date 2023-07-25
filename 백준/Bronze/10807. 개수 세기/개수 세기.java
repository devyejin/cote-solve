import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {


        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {

            int length = Integer.parseInt(br.readLine());
            String[] arr = br.readLine().split(" ");
            String keyword = br.readLine();
            int count = 0;

            for(int i=0; i<length; i++) {
                if(keyword.equals(arr[i])) count++;
            }

            System.out.println(count);


        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}