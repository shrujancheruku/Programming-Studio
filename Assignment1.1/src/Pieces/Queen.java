package Pieces;

import Logic.Board;

import java.awt.*;

/**
 * @author Shrujan Cheruku
 *         A Queen class. It extends Piece and adds a constructor along with the moveset
 */
public class Queen extends Piece {
    /**
    *Constructor for the Queen class.
    *Uses the Piece constructor but adds Queen specific moves to the moveSet.
    *@param: isWhite and position
    *@return: none
    **/
    public Queen(boolean isWhite, Point position) {
        super(isWhite, position);

        //adding the rook moves along the horizontal plane
        for (int x = 1; x < Board.width; x++) {
            moveSet.add(new Point(x, 0));
            moveSet.add(new Point(-1 * x, 0));
        }

        //adding the rook moves along the vertical plane
        for (int y = 1; y < Board.height; y++) {
            moveSet.add(new Point(0, y));
            moveSet.add(new Point(0, -1 * y));
        }

        //adding the bishop moves along the diagonals
        for (int x = 1; x < Board.width; x++) {
            for (int y = 1; y < Board.height; y++) {
                if (x == y) {
                    moveSet.add(new Point(x, y));
                    moveSet.add(new Point(-1 * x, y));
                    moveSet.add(new Point(x, -1 * y));
                    moveSet.add(new Point(-1 * x, -1 * y));
                }
            }
        }
    }
}
