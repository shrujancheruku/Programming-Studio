package Pieces;

import Logic.Board;

import java.awt.*;

/**
 * @author Shrujan Cheruku
 */
public class Princess extends Piece{
    /**
     *Constructor for the Princess class.
     *Uses the Piece constructor but adds Princess specific moves to the moveSet.
     *@param: isWhite and position
     *@return: none
     **/
    public Princess(boolean isWhite, Point position) {
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
