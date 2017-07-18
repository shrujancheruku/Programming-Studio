import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 *@author Shrujan Cheruku
 */
public class KingTest {
    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        King testKing = new King(true, testPoint);
        Point movePoint = new Point(5, 2);
        assertTrue(testKing.move(movePoint));
        assertTrue(testKing.getPosition().equals(movePoint));
        Point movePoint2 = new Point(6,4);
        assertFalse(testKing.move(movePoint2));
        assertFalse(testKing.getPosition().equals(movePoint2));
        assertTrue(testKing.getPosition().equals(movePoint));
        Point movePoint3 = new Point(5, 3);
        assertTrue(testKing.move(movePoint3));
        assertTrue(testKing.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        King testKing = new King(true, testPoint);
        assertTrue(testKing.getPosition().equals(testPoint));

        Point movePoint = new Point(5, 2);
        assertTrue(testKing.move(movePoint));
        Point testPoint2 = new Point(5,2);
        assertTrue(testKing.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testKing.move(illegalMovePoint));
        assertTrue(testKing.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");
    }

}