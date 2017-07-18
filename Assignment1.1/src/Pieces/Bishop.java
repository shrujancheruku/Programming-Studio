package Pieces;

import Logic.Board;

import java.awt.*;

/**
 *@author Shrujan Cheruku
 *        A Bishop class. It extends Piece and adds a constructor along with the moveset
 */
public class Bishop extends Piece{

    /**
    *Constructor for the Bishop class.
    *Uses the Piece constructor but adds Bishop specific moves to the moveSet.
    *@param: isWhite and position
    *@return: none
    **/
    public Bishop(boolean isWhite, Point position) {
        super(isWhite, position);

        //iterate over the entire board, and add all diagonal moves.
        //it adds moves starting from the center and spreading out in all four directions
        for (int x = 1; x < Board.width; x++) {
            for (int y = 1; y < Board.height; y++) {
                if(x == y) {
                    //first quadrant
                    moveSet.add(new Point(x, y));
                    //second quadrant
                    moveSet.add(new Point(x, -1 * y));
                    //third quadrant
                    moveSet.add(new Point(-1 * x, -1 * y));
                    //fourth quadrant
                    moveSet.add(new Point(-1 * x, y));
                }
            }
        }
    }
}
