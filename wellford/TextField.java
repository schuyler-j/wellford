package wellford;

import javax.swing.*;
import javax.swing.JTextArea;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.sql.SQLOutput;

public class TextField extends JFrame implements KeyListener {

    JTextArea textArea = new JTextArea(5, 15);
    JTextField textField = new JTextField(15);
    public void TextField() {

        JFrame frame = new JFrame();
        Graphic graph = new Graphic();

        graph.setBackground(Color.black);

        textField.addKeyListener(this);

        Container content = frame.getContentPane();
        content.add(graph);

        textArea.setForeground(Color.white);
        textArea.setEditable(false);
        textArea.setLineWrap(true);
        textArea.setBackground(Color.darkGray);
        textField.setBackground(Color.black);
        textField.setForeground(Color.white);
        frame.add(textArea);
        frame.add(textField);


        frame.setTitle("CLASS APP");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setExtendedState(MAXIMIZED_BOTH);
        frame.setLocationRelativeTo(null);


        frame.setLayout(new GridLayout());


        ///frame.add(test);
        /// test.add(tested);

    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        if(key == KeyEvent.VK_ENTER){
            String text = textField.getText();
            textArea.append(text);
        }

        if(key == KeyEvent.VK_DELETE){
            textArea.setText("");
        }

        if(key == KeyEvent.VK_CONTROL){
        }

    }

    @Override
    public void keyReleased(KeyEvent e) {

    }
}
