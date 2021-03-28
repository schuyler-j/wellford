package schu0527;

import javax.swing.*;
import java.awt.*;

public class Frame{

    public static void main(String[] args) {

        JFrame frame = new JFrame();

        Graphic graph = new Graphic();
        TextField panel = new TextField();


        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setSize(480, 640);
        frame.add(panel);
        frame.add(graph);
        frame.setTitle("CLASS APP");




        ///frame.add(test);
       /// test.add(tested);






    }
}