package Tests;

import Pieces.Empress;
import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author Shrujan Cheruku
 */
public class EmpressTest {
    @Test
    /**
     *Check to see if move() is working correctly
     *@param: none
     *@return: none
     **/
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Empress testEmpress = new Empress(true, testPoint);
        Point movePoint = new Point(6, 3);
        assertTrue(testEmpress.move(movePoint));
        assertTrue(testEmpress.getPosition().equals(movePoint));
        Point movePoint2 = new Point(7,7);
        assertFalse(testEmpress.move(movePoint2));
        assertFalse(testEmpress.getPosition().equals(movePoint2));
        assertTrue(testEmpress.getPosition().equals(movePoint));
        Point movePoint3 = new Point(4, 2);
        assertTrue(testEmpress.move(movePoint3));
        assertTrue(testEmpress.getPosition().equals(movePoint3));

        System.out.println("Passed move() testing");

    }

    @Test
    /**
     *Check to see if getPosition() is working
     *@param: none
     *@return: none
     **/
    public void getPosition() throws Exception {
        Point testPoint = new Point(5, 1);
        Empress testEmpress = new Empress(true, testPoint);
        assertTrue(testEmpress.getPosition().equals(testPoint));

        Point movePoint = new Point(6, 3);
        assertTrue(testEmpress.move(movePoint));
        Point testPoint2 = new Point(6,3);
        assertTrue(testEmpress.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testEmpress.move(illegalMovePoint));
        assertTrue(testEmpress.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");
    }

}