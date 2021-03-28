package schu0527;

import javax.swing.*;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.TextEvent;
import java.awt.event.TextListener;

public class TextField extends JPanel implements ActionListener{
    /**
     *
     */
    private static final long serialVersionUID = 1L;
    private final static String newLine = "\n";


    public txtField() {

        ///JTextField text = new JTextField(15);
        ///text.addActionListener(this);

        JTextArea textArea = new JTextArea(5, 15);

        JPanel jp = new JPanel();

        jp.add(textArea);
        jp.setSize(20, 20);



    }


    @Override
   public void actionPerformed(ActionEvent e) {

   }
}
