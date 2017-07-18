import java.awt.*;

/**
 * @author Shrujan Cheruku
 *         A Rook class. It extends Piece and adds a constructor along with the moveset
 */

class Rook extends Piece {
    /*
    *Constructor for the Rook class.
    *Uses the Piece constructor but adds Rook specific moves to the moveSet.
    *@param: isWhite and position
    *@return: none
    */
    Rook(boolean isWhite, Point position) {
        super(isWhite, position);

        //adding moves across the horizontal plane
        for (int x = 1; x < Board.width; x++) {
            moveSet.add(new Point(x, 0));
            moveSet.add(new Point(-1 * x, 0));
        }

        //adding moves across the vertical plane
        for (int y = 1; y < Board.height; y++) {
            moveSet.add(new Point(0, y));
            moveSet.add(new Point(0, -1 * y));
        }
    }
}
