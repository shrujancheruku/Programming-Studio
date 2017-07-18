import java.awt.*;

/**
 * @author Shrujan Cheruku
 *         A blank space class to take up positions on the board
 */
public class Blank extends Piece {

    /*
    *Constructor for the Blank class.
    *Uses the Piece constructor. Since this class has no functionality it needs no moveSet
    *@param: position
    *@return: none
    */
    Blank(Point position){
        super(false, position); }
}
