package GUI;

import javax.swing.*;
import java.awt.*;

/**
 *@author Shrujan Cheruku
 */
class GUI {

    static JFrame mainframe = new JFrame();
    private GridLayout grid = new GridLayout(8, 8);

    /**
     *Constructor for the GUI class.
     *Sets up the mainframe
     *@param: none
     *@return: none
     **/
    GUI() {
        mainframe.setSize(700, 700);
        mainframe.setLayout(grid);
        mainframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
