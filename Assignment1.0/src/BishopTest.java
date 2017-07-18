import org.junit.Test;

import java.awt.*;
import java.util.Vector;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author Shrujan Cheruku
 */
public class BishopTest {
    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Bishop testBishop = new Bishop(true, testPoint);
        Point movePoint = new Point(7, 3);
        assertTrue(testBishop.move(movePoint));
        assertTrue(testBishop.getPosition().equals(movePoint));
        Point movePoint2 = new Point(7,4);
        assertFalse(testBishop.move(movePoint2));
        assertFalse(testBishop.getPosition().equals(movePoint2));
        Point movePoint3 = new Point(4, 0);
        assertTrue(testBishop.move(movePoint3));
        assertTrue(testBishop.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Bishop testBishop = new Bishop(true, testPoint);
        assertTrue(testBishop.getPosition().equals(testPoint));

        Point movePoint = new Point(7, 3);
        assertTrue(testBishop.move(movePoint));
        Point testPoint2 = new Point(7,3);
        assertTrue(testBishop.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testBishop.move(illegalMovePoint));
        assertTrue(testBishop.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");
    }

    @Test
    public void getLegalMoves() throws Exception {
        Point testPoint = new Point(5, 1);
        Bishop testBishop = new Bishop(true, testPoint);
        Vector testVector = testBishop.getLegalMoves();
        assertTrue(testVector.size() == 9);
        Point movePoint = new Point(7, 3);
        assertTrue(testBishop.move(movePoint));
        testVector = testBishop.getLegalMoves();
        assertTrue(testVector.size() == 7);

        System.out.println("Passed getLegalMoves() testing");

    }

}