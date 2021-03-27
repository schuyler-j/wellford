
import java.util.Scanner;


public class Main{

    public static void main(String[] args){
        
        Scanner scan = new Scanner(System.in);
        
        int biscuits1;
        
        System.out.println("Enter the number of biscuits");
        biscuits1 = scan.nextInt();
        
        int packet1, box1, leftover1, remainder1;

        String is = "is";
        String are = "are";

        String box = "box";
        String boxes = "boxes";

        String biscuit = "biscuit";
        String biscuits = "biscuits";

        String packet = "packet";
        String packets = "packets";
        
        String packetA = "";

        packet1 = biscuits1 / 12;
        remainder1 = packet1 % 30;
        box1 = packet1 / 30;
        leftover1 = biscuits1 % 12;



        String a = "";
        String b = "";
        String c = "";
        String d = "";


        if(packet1 == 1){
            are = "is";
        }
        if(packet1 > 1 || packet1 == 0){
            packet = "packets";
        }
        if(packet1 == 0){
            a = "no";
        }
        if(box1 > 1){
            box = "boxes";
        }
        if(box1 == 0){
            b = "no";
        }
        if(box1 == 0){
            box = "boxes";
        }
        if(packet1 == 1){
            packetA = "packet";
        }
        if(packet1 > 1){
            packetA = "packets";
        }
        if(leftover1 == 0){
            c = "no";
        }
        if(leftover1 == 1){
            packet = "packet";
        }
        if(leftover1 == 1){
            packetA = "packets";
        }
        if(leftover1 > 1){
            packetA = "packets";
        }
        if(leftover1 == 0){
            packetA = "packets";
        }
        if(remainder1 > 1){
            biscuit = "biscuits";
        }
        if(remainder1 == 1){
            biscuit = "biscuits";
        }
        if(remainder1 == 0){
            biscuit = "biscuits";
        }
        if(remainder1 == 0){
            d = "no";
        }
        
        if(remainder1 == 1){
            packetA = "packet";
        }
        if(leftover1 == 1){
            packet = "packets";
        }
        if(leftover1 == 1){
            biscuit = "biscuit";
        }

        
        

        if(packet1 > 0){
            a = String.valueOf(packet1);
        }
        if(box1 > 0){
            b = String.valueOf(box1);
        }
        if(leftover1 > 0){
            c = String.valueOf(leftover1);
        }
        if(remainder1 > 0){
            d = String.valueOf(remainder1);
        }


        System.out.println("There " + are + " " + a + " " + packetA + " of " + biscuit + " : " + b + " " + box + " with " + d + " leftover " + packet + " and " + c + " leftover " + biscuit);


        ///There are/is x/no packet/s of biscuit/s: x/no box/es with x/no leftover packet/s and x/no leftover biscuit/s

        
    }
}
