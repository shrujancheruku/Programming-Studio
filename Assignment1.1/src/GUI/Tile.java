package GUI;

import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;

/**
 *@author Shrujan Cheruku
 */

class Tile {
    JLabel lbl = new JLabel();
    private static Font unicode = new Font("Tahoma", Font.BOLD, 50);
    private static LineBorder border = new LineBorder(Color.BLACK, 2);

    /**
     *Constructor for the Tile class.
     *Sets the piece (if any) as well as the color of the tile
     *@param: labelName and tileColor
     *@return: none
     **/
    Tile(String labelName, Color tileColor) {
        lbl.setFont(unicode);
        lbl.setHorizontalAlignment(JLabel.CENTER);
        lbl.setText(labelName);
        lbl.setBackground(tileColor);
        lbl.setBorder(border);
        lbl.setOpaque(true);
    }
}
