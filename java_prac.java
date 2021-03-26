package practical03;

import java.util.Scanner;

public class Bis {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String first, second, third, fourth;

        // declare any variables here
        int biscuits, packet, box, remainder, leftover;

        // prompt for the number of biscuits
        System.out.println("Enter the number of biscuits");
        biscuits = scan.nextInt();

        ///math
        packet = biscuits / 12;
        remainder = packet % 30;
        box = packet / 30;
        leftover = biscuits % 12;

        ///initial strings
        first = "There";
        third = " packets of";
        second = " box";
        fourth = " packets";
        String plural = " packets of biscuits: ";

        ///zeros and ones
        if(leftover == 1){
            third = " 1 leftover biscuit";
        }
        if(leftover == 0){
            third = " no leftover biscuits";
        }

        if(box == 1){
            second = " 1 box ";
        }
        if(box == 0){
            second = " no boxes ";
        }

        if(remainder == 0){
            fourth = " no leftover packets ";
        }
        if(remainder == 1){
            fourth = " 1 leftover packet ";
        }

        if(packet == 0){
            plural = " are no packets of biscuits:";
        }
        if(packet == 1){
            plural = " is 1 packet of biscuits:";
        }

        if(packet > 1){
            plural = " packets of biscuits: ";
        }
        if(remainder > 1){
            fourth = " leftover packets ";
        }
        if(box > 1){
            second = " boxes";
        }
        if(leftover > 1){
            third = " leftover biscuits";
        }

        ///print these for checking (not a part of code)
        System.out.println(packet + "packet");
        System.out.println(remainder + "remainder");///leftover biscuits
        System.out.println(box + "box"); ///boxes
        System.out.println(leftover + "leftover"); ///packets leftover


        if(packet > 1 && remainder > 1 && box > 1 && leftover > 1){
            System.out.println(first + " are " + packet + plural + box + second + " with " + remainder + fourth + "and " + leftover + third);
        }
        if(packet > 1 && box > 1 && leftover > 1){
            System.out.println(first + " are " + packet + plural + box + second + " with" + fourth + "and " + leftover + third);
        }
        if(packet > 1 && box > 1){
            System.out.println(first + " are " + packet + plural + box + second + " with" + fourth + "and " + third);
        }
        if(packet > 1){
            System.out.println(first + " are " + packet + plural + second + "with" + fourth + "and " + third);
        }

        if(packet > 1 && remainder > 1 && leftover > 1){
            System.out.println(first + " are " + packet + plural + second + "with " + remainder + fourth + "and " + leftover + third);
        }
        if(packet > 1 && remainder > 1){
            System.out.println(first + " are " + packet + plural + second + "with " + remainder + fourth + "and " + third);
        }
        if(packet > 1 && leftover > 1){
            System.out.println(first + " are " + packet + plural + second + "with" + fourth + "and " + leftover + third);
        }

        if(leftover > 1){
            System.out.println(first +  plural + second + "with" + fourth + "and " + leftover + third);
        }



        System.out.println(first + plural + second + "with" + fourth + "and" + third);


    }
}
