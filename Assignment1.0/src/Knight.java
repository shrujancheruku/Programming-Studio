import java.awt.*;

/**
 *@author Shrujan Cheruku
 *        A Knight class. It extends Piece and adds a constructor along with the moveset
 */
public class Knight extends Piece{
    /*
   *Constructor for the Knight class.
   *Uses the Piece constructor but adds Knight specific moves to the moveSet.
   *@param: isWhite and position
   *@return: none
   */
    Knight(boolean isWhite, Point position) {
        super(isWhite, position);

        //adding the L shaped moves
        //these move one sideways and two upwards
        moveSet.add(new Point(1, 2));
        moveSet.add(new Point(-1, 2));
        //these move two sideways and one upwards
        moveSet.add(new Point(2, 1));
        moveSet.add(new Point(-2, 1));
        //these move one sideways and two downwards
        moveSet.add(new Point(1, -2));
        moveSet.add(new Point(-1, -2));
        //these move two sideways and one downwards
        moveSet.add(new Point(2, -1));
        moveSet.add(new Point(-2, -1));
    }
}
