import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        int weight, carrier = 0, count = 0, max = 0;
        Scanner sc = new Scanner(System.in);
        int[] maxpacket = new int[100];
        do {
            weight = sc.nextInt();

            if (weight + carrier > 30 || weight == 0) {
                System.out.println("> " + carrier);
                carrier = weight;
                maxpacket[count] = max;
                count++;
                max = 0;
            } else {
                carrier += weight;
            }
            if (max < weight) {
                max = weight;
            }
        } while (weight != 0);
        for (int i = 0; i < count; i++)
            System.out.println(maxpacket[i]);
    }
}