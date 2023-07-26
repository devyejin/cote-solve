import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {


        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {

            int x = Integer.parseInt(br.readLine());
            int y = Integer.parseInt(br.readLine());

            int[] Quadrant = {1, 2, 3, 4};
            int result = 0;

            if (x > 0) {
                if (y > 0) result = Quadrant[0]; 
                else result = Quadrant[3]; 
            } else {
                if (y > 0) result = Quadrant[1]; 
                else result = Quadrant[2]; 
            }

            System.out.println(result);


        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}