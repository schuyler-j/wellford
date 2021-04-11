package wellford;

import org.w3c.dom.css.RGBColor;

import javax.swing.*;
import javax.swing.JTextArea;
import java.awt.*;
import java.awt.event.*;
import java.sql.SQLOutput;

public class TextField extends JFrame implements KeyListener {

    JTextArea textArea = new JTextArea(5, 15);
    JTextField textField = new JTextField(15);
    Graphic graph = new Graphic();
    public void TextField() {

        JFrame frame = new JFrame();

        graph.setBackground(Color.getHSBColor(285,482, 100));

        textField.addKeyListener(this);

        Container content = frame.getContentPane();
        content.setLayout(new GridLayout());

        content.add(graph);
        textArea.setEditable(false);
        textArea.setLineWrap(true);
        textArea.setBackground(Color.getHSBColor(305,200, 45));
        textField.setBackground(Color.getHSBColor(34,100, 5));
        frame.add(textArea);
        frame.add(textField);



        frame.setTitle("CLASS APP");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setExtendedState(MAXIMIZED_BOTH);
        frame.setLocationRelativeTo(null);


        ///frame.add(test);
        /// test.add(tested);

    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        String newline = "\n";

        if(key == KeyEvent.VK_ENTER){
            String text = textField.getText();
            textArea.append(text);
            textField.setText(null);
            textArea.append(newline);

            graph.label1 = text;

            if(text.equals("clear")){
                textArea.setText("");
            }

        }

        if(key == KeyEvent.VK_DELETE){
            textArea.setText("");
        }

        if(key == KeyEvent.VK_CONTROL){
            textArea.append(newline);
        }

    }

    @Override
    public void keyReleased(KeyEvent e) {

    }
}
