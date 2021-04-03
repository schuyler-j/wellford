package wellford;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.Serial;
import java.util.EventListener;
import java.util.Random;


public class Graphic extends JPanel implements ActionListener {

    /**
     *
     */
    @Serial
    private static final long serialVersionUID = 1L;

    Timer tm = new Timer(50, this);
    int x = 0, velX = 2, y = 0;

    int a, b, c, d;

    public void paintComponent(Graphics g) {

        super.paintComponent(g);

        Graphics2D g2D = (Graphics2D) g;
        //draw the titles
        g2D.setColor(Color.white);
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
        g2D.fillRect(c, d, 15, 15);

        g2D.setColor(Color.orange);
        g2D.fillRect(x, 330, 250, 5);

        //draw the lines
        g2D.setColor(Color.BLUE);
        g2D.drawLine(10, 50, 150, 50);
        g2D.drawLine(10, 150, 150, 150);
        g2D.drawLine(10, 100, 150, 100);

        g2D.drawLine(150, 50, 150, 150);
        g2D.drawLine(10, 50, 10, 150);
        g2D.drawLine(80, 50, 80, 150);

        boolean now = false;

        if(a > 50 && a < 150){
            this.delete(g);
            c = a;
            d = b;
        }

        if(!now){
            now = true;
        }



        //start the timer
        tm.start();

    }

    @Override
    public void actionPerformed(ActionEvent e) {

        PointerInfo mouse = MouseInfo.getPointerInfo();
        Point m = mouse.getLocation();
        a = (int) m.getX();
        b = (int) m.getY();

        c = 1000;
        d = 1000;

        x = x + velX;

        repaint();
        if(x > 80){
            x = 0;
        }

    }

    public void hover(Graphics g){

        g.fillRect(100, 150, 110, 30);


    }
    public void delete(Graphics g){

        g.setColor(Color.green);
        g.fillRect(100, 280, 30, 30);


    }

}