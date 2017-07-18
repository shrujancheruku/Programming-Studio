import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 *@author Shrujan Cheruku
 */
public class KnightTest {
    @Test
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Knight testKnight = new Knight(true, testPoint);
        Point movePoint = new Point(6, 3);
        assertTrue(testKnight.move(movePoint));
        assertTrue(testKnight.getPosition().equals(movePoint));
        Point movePoint2 = new Point(6,4);
        assertFalse(testKnight.move(movePoint2));
        assertFalse(testKnight.getPosition().equals(movePoint2));
        assertTrue(testKnight.getPosition().equals(movePoint));
        Point movePoint3 = new Point(4, 2);
        assertTrue(testKnight.move(movePoint3));
        assertTrue(testKnight.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");
    }

    @Test
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Knight testKnight = new Knight(true, testPoint);
        assertTrue(testKnight.getPosition().equals(testPoint));

        Point movePoint = new Point(6, 3);
        assertTrue(testKnight.move(movePoint));
        Point testPoint2 = new Point(6,3);
        assertTrue(testKnight.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testKnight.move(illegalMovePoint));
        assertTrue(testKnight.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");

    }

}