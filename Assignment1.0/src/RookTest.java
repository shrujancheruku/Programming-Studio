import org.junit.Test;

import java.awt.*;
import java.util.Vector;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author Shrujan Cheruku
 */

public class RookTest {
    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Rook testRook = new Rook(true, testPoint);
        Point movePoint = new Point(5, 3);
        assertTrue(testRook.move(movePoint));
        assertTrue(testRook.getPosition().equals(movePoint));
        Point movePoint2 = new Point(6,7);
        assertFalse(testRook.move(movePoint2));
        assertFalse(testRook.getPosition().equals(movePoint2));
        Point movePoint3 = new Point(1, 3);
        assertTrue(testRook.move(movePoint3));
        assertTrue(testRook.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getLegalMoves() throws Exception {
        Point testPoint = new Point(5, 1);
        Rook testRook = new Rook(true, testPoint);
        Vector testVector = testRook.getLegalMoves();
        assertTrue(testVector.size() == 14);
        Point movePoint = new Point(5, 3);
        assertTrue(testRook.move(movePoint));
        testVector = testRook.getLegalMoves();
        assertTrue(testVector.size() == 14);

        System.out.println("Passed getLegalMoves() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Rook testRook = new Rook(true, testPoint);
        assertTrue(testRook.getPosition().equals(testPoint));

        Point movePoint = new Point(5, 3);
        assertTrue(testRook.move(movePoint));
        Point testPoint2 = new Point(5,3);
        assertTrue(testRook.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testRook.move(illegalMovePoint));
        assertTrue(testRook.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");

    }

}