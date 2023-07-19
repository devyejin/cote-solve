import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 드모르간~ 같을거같은데!
 */
public class Main {
    public static void main(String[] args) {

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            int length = st.countTokens();
            int[] nums = new int[length];

            for(int i=0; i<length; i++) {
                if(st.hasMoreTokens())
                    nums[i] = Integer.parseInt(st.nextToken());
            }

            int A = nums[0]; int B = nums[1]; int C = nums[2];

            printResult(A, B, C);


        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    private static void printResult(int A, int B, int C) {
        System.out.println((A + B)% C);
        System.out.println(((A % C) + (B % C))% C);
        System.out.println( (A * B)% C);
        System.out.println(((A % C)*(B % C))% C);
    }
    
}