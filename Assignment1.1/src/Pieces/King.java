package Pieces;

import java.awt.*;

/**
 *@author Shrujan Cheruku
 *        A King class. It extends Piece and adds a constructor along with the moveset
 */
public class King extends Piece{
    /**
    *Constructor for the King class.
    *Uses the Piece constructor but adds King specific moves to the moveSet.
    *@param: isWhite and position
    *@return: none
    **/
    public King(boolean isWhite, Point position) {
        super(isWhite, position);
        isKing = true; //change isKing

        //adding single steps in all eight directions
        moveSet.add(new Point(0, 1));
        moveSet.add(new Point(0, -1));
        moveSet.add(new Point(1, 0));
        moveSet.add(new Point(-1, 0));
        moveSet.add(new Point(1, 1));
        moveSet.add(new Point(1, -1));
        moveSet.add(new Point(-1, 1));
        moveSet.add(new Point(-1, -1));

    }
}
