package Pieces;

import Logic.Board;

import java.awt.*;

/**
 * @author Shrujan Cheruku
 */
public class Empress extends Piece{
        /**
         *Constructor for the Empress class.
         *Uses the Piece constructor but adds Empress specific moves to the moveSet.
         *@param: isWhite and position
         *@return: none
         **/
        public Empress(boolean isWhite, Point position) {
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
