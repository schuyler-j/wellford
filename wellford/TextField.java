package wellford;

import javax.swing.*;
import javax.swing.JTextArea;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TextField extends JFrame implements ActionListener {

    TextField() {

        JFrame frame = new JFrame();
        Graphic graph = new Graphic();

        graph.setBackground(Color.black);

        JTextArea textArea = new JTextArea(5, 15);
        JTextField textField = new JTextField(15);

        Container content = frame.getContentPane();
        content.add(graph);

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
        frame.setSize(880, 440);
        frame.setLocationRelativeTo(null);


        frame.setLayout(new GridLayout());


        ///frame.add(test);
        /// test.add(tested);

    }
    public void actionPerformed(ActionEvent e) {

    }

}
