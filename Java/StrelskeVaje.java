import java.util.Scanner;

public class StrelskeVaje {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Vpisi gravitacijski pospesek");
        double g = sc.nextDouble();
        System.out.println("Vpisi hitrost");
        double v = sc.nextDouble();
        System.out.println("Vpisi kot");
        double kot = sc.nextDouble();
        double s = (Math.pow(v, 2) * Math.sin(2 * Math.toRadians(kot))) / g;
        System.out.println("Krogle bo letela " + s + "m");
        sc.close();
    }
}