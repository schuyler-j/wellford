package wellford;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class Mouse extends TextField implements MouseListener {

    @Override
    public void mouseClicked(MouseEvent e) {
       graph.hover(getGraphics());

    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}
