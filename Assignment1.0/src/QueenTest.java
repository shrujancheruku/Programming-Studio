import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 *@author Shrujan Cheruku
 */
public class QueenTest {
    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Queen testQueen = new Queen(true, testPoint);
        Point movePoint = new Point(7, 3);
        assertTrue(testQueen.move(movePoint));
        assertTrue(testQueen.getPosition().equals(movePoint));
        Point movePoint2 = new Point(6,1);
        assertFalse(testQueen.move(movePoint2));
        assertFalse(testQueen.getPosition().equals(movePoint2));
        assertTrue(testQueen.getPosition().equals(movePoint));
        Point movePoint3 = new Point(7, 5);
        assertTrue(testQueen.move(movePoint3));
        assertTrue(testQueen.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Queen testQueen = new Queen(true, testPoint);
        assertTrue(testQueen.getPosition().equals(testPoint));

        Point movePoint = new Point(1, 1);
        assertTrue(testQueen.move(movePoint));
        Point testPoint2 = new Point(1,1);
        assertTrue(testQueen.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testQueen.move(illegalMovePoint));
        assertTrue(testQueen.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");

    }

}