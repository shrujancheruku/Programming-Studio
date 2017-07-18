import java.awt.*;
import java.util.Vector;

/**
 * @author Shrujan Cheruku
 *         Generic piece class designed to be extended further for each specific piece.
 *         Contains functions and variables that are common between pieces.
 */

public abstract class Piece {

    private boolean isWhite; //true if white, false if black
    boolean isKing = false; //only true if the piece is the King
    private Point position = new Point();
    Vector moveSet = new Vector(); //Vector of moves from position (0 , 0)

    /*
     *A basic constructor for the Piece class
     *@param: isWhite and starting position
     *@return: none
     */
    Piece(boolean isWhite, Point position) {
        this.isWhite = isWhite;
        this.position = position;
    }

    /*
     *Move the piece to a Point on the board
     *@param: newPosition
     *@return: true if the move is legal, false if not
     */
    boolean move(Point newPosition) {
        if (getLegalMoves().contains(newPosition)) {
            position = newPosition;
            return true;
        }
        return false;
    }

    /*
    *A getter function for the current position
    *@param: none
    *@return: A Point of the piece's current position
    */
    Point getPosition() {
        return position;
    }


    /*
    *A getter function for isWhite
    *@param: none
    *@return: true if white, false if not
    */
    public boolean getIsWhite() {
        return isWhite;
    }

    /*
    *Return a vector of legal moves based on the current position
    *Calculated using the specified moveSet
    *@param: none
    *@return: a vector of Points to legal move positions
    */
    Vector getLegalMoves() {
        Vector legalMoves = new Vector();
        for (int i = 0; i < moveSet.size(); i++) {
            //iterate over the moveSet
            Point movePoint = Board.addPoints(getPosition(), (Point) moveSet.elementAt(i));
            if ((movePoint.x <= Board.width && movePoint.x >= 0) && (movePoint.y <= Board.height && movePoint.y >= 0))
                //add the move position to the Vector only if it fits in the board dimensions
                legalMoves.add(movePoint);
        }
        return legalMoves;
    }
}
