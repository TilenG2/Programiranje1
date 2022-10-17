import java.util.Scanner;

public class MovNosac {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] coordinati = new int[2];
        String str;
        char c;
        int mov;
        while (true) {
            str = sc.next();

            if (str.length() > 2) {
                continue;
            } else if (str.equals(".."))
                break;

            c = str.charAt(0);
            str = str.charAt(1) + "";
            mov = Integer.parseInt(str);
            if (c == '>') {
                coordinati[0] += mov;
            } else if (c == '<') {
                coordinati[0] -= mov;
            } else if (c == '^') {
                coordinati[1] += mov;
            } else if (c == 'v') {
                coordinati[1] -= mov;
            }
        }
        System.out.println("(" + coordinati[0] + ", " + coordinati[1] + ")");
    }
}