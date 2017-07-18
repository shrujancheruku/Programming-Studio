package Pieces;

import Logic.Board;

import java.awt.*;
import java.util.Vector;

/**
 *@author Shrujan Cheruku
 *        A Pawn class. It extends Piece and adds a constructor along with the moveset
 */

/**
 *TODO  Implement moving diagonally for capturing pieces
 */

public class Pawn extends Piece {
    /**
    *Constructor for the Pawn class.
    *Uses the Piece constructor but adds Pawn specific moves to the moveSet.
    *@param: isWhite and position
    *@return: none
    **/
    public Pawn(boolean isWhite, Point position) {
        super(isWhite, position);

        //define separate moveSet for white and black pawns, since they can't move backwards
        if (isWhite) {
            moveSet.add(new Point(0, 1));
            moveSet.add(new Point(0, 2));
        } else {
            moveSet.add(new Point(0, -1));
            moveSet.add(new Point(0, -2));
        }
    }

    /**
    *Check to see if the pawn has been moved from it's starting position
    *This is important because the pawn can move two steps on it's first turn only
    *@param: none
    *@return: true if it has moved, false if not
    **/
    public boolean hasMoved() {
        if (this.getIsWhite()) {
            if (getPosition().y == 1)
                return false;
        } else {
            if (getPosition().y == (Board.height - 1))
                return false;
        }

        return true;
    }

    /**
    *Return Overriding the parent function, since pawns can move twice on their first turn only
    *This means that if hasMoved() returns true then we disregard the second half of the moveSet
    *@param: none
    *@return: a vector of Points to legal move positions
    **/
    public Vector getLegalMoves() {
        Vector legalMoves = new Vector();

        int canMoveTwo; //iterator that determines if we use the entire moveSet or not

        if (hasMoved()) {
            canMoveTwo = 1;
        } else {
            canMoveTwo = 2;
        }

        for (int x = 0; x < canMoveTwo; x++) {
            Point movePoint = Board.addPoints(getPosition(), (Point) moveSet.elementAt(x));

            if (movePoint.x <= Board.width && movePoint.y <= Board.height)
                legalMoves.add(movePoint);
        }

        return legalMoves;
    }
}
