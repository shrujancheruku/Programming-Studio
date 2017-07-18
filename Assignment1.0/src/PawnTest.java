import org.junit.Test;

import java.awt.*;
import java.util.Vector;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author Shrujan Cheruku
 */

public class PawnTest {
    @Test
    public void hasMoved() throws Exception {
        Point testPoint = new Point(5, 1);
        Pawn testPawn = new Pawn(true, testPoint);
        assertFalse(testPawn.hasMoved());

        Point movePoint = new Point(5, 3);
        assertTrue(testPawn.move(movePoint));
        assertTrue(testPawn.hasMoved());

        System.out.println("Passed hasMoved() testing");
    }

    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Pawn testPawn = new Pawn(true, testPoint);
        Point movePoint = new Point(5, 3);
        assertTrue(testPawn.move(movePoint));
        assertTrue(testPawn.getPosition().equals(movePoint));
        Point movePoint2 = new Point(5,5);
        assertFalse(testPawn.move(movePoint2));
        assertFalse(testPawn.getPosition().equals(movePoint2));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getLegalMoves() throws Exception {
        Point testPoint = new Point(5, 1);
        Pawn testPawn = new Pawn(true, testPoint);
        Vector testVector = testPawn.getLegalMoves();
        assertTrue(testVector.size() == 2);
        Point movePoint = new Point(5, 3);
        assertTrue(testPawn.move(movePoint));
        testVector = testPawn.getLegalMoves();
        assertTrue(testVector.size() == 1);

        System.out.println("Passed getLegalMoves() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Pawn testPawn = new Pawn(true, testPoint);
        Point testPoint1 = new Point(5,1);
        assertTrue(testPawn.getPosition().equals(testPoint1));

        Point movePoint = new Point(5, 3);
        assertTrue(testPawn.move(movePoint));
        Point testPoint2 = new Point(5,3);
        assertTrue(testPawn.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testPawn.move(illegalMovePoint));
        assertTrue(testPawn.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");

    }

}