package schu0527;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;


public class Graphic extends JPanel implements ActionListener {

    /**
     *
     */
    private static final long serialVersionUID = 1L;

    Timer tm = new Timer(50, this);
    int x = 0, velX = 2, y = 0;


    public void paintComponent(Graphics g) {

        super.paintComponent(g);

        Graphics2D g2D = (Graphics2D) g;
        //draw the titles
        g2D.drawString("DATA SCIENCE", 40, 180);
        g2D.drawString("COMPUTATIONAL INTELLIGENCE", 40, 200);
        g2D.drawString("COMPUTER PROGRAMMING", 40, 220);
        g2D.drawString("PSYCHOLOGY", 40, 240);

        //draw the boxes
        g2D.setColor(Color.ORANGE);
        g2D.fillRect(30, 55, 30, 30);
        g2D.setColor(Color.GREEN);
        g2D.fillRect(100, 55, 30, 30);
        g2D.setColor(Color.BLUE);
        g2D.fillRect(100, 110, 30, 30);
        g2D.setColor(Color.RED);
        g2D.fillRect(30, 130, 15, 15);

        //draw the lines
        g2D.setColor(Color.BLUE);
        g2D.drawLine(10, 50, 150, 50);
        g2D.drawLine(10, 150, 150, 150);
        g2D.drawLine(10, 100, 150, 100);

        g2D.drawLine(150, 50, 150, 150);
        g2D.drawLine(10, 50, 10, 150);
        g2D.drawLine(80, 50, 80, 150);

        //start the timer
        tm.start();

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Random $g = new Random(10);

        int y = $g.nextInt();

        x = x + velX;
        repaint();
        if(x > 280){
            x = 0;
        }

    }
}