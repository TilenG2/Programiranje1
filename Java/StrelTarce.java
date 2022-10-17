import java.util.Scanner;

public class StrelTarce {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double g = 9.807, v, kot, s;
        System.out.println("Vpisi oddaljenost tarce");
        double target = sc.nextDouble();
        System.out.println("Vpisoval bos hitrost(v) in kot(L) dokler ne bos v 1m tarce \nGood Luck!");
        while (true) {
            System.out.print("v:");
            v = sc.nextDouble();
            System.out.print("L:");
            kot = sc.nextDouble();
            s = (Math.pow(v, 2) * Math.sin(2 * Math.toRadians(kot))) / g;
            if (target-- < s && target++ > s) {
                System.out.println("Bravo zadel si tarco");
                break;
            }
            System.out.println("Tarco si zgresil za " + Math.abs(target - s) + "m");
        }
        sc.close();
    }
}