package Tests;

import Pieces.Princess;
import org.junit.Test;

import java.awt.*;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author Shrujan Cheruku
 */
public class PrincessTest {
    @Test
    /**
     *Check to see if move() is working correctly
     *@param: none
     *@return: none
     **/
    public void move() throws Exception {
        Point testPoint = new Point(5, 1);
        Princess testPrincess = new Princess(true, testPoint);
        Point movePoint = new Point(6, 3);
        assertTrue(testPrincess.move(movePoint));
        assertTrue(testPrincess.getPosition().equals(movePoint));
        Point movePoint2 = new Point(7,7);
        assertFalse(testPrincess.move(movePoint2));
        assertFalse(testPrincess.getPosition().equals(movePoint2));
        assertTrue(testPrincess.getPosition().equals(movePoint));
        Point movePoint3 = new Point(4, 2);
        assertTrue(testPrincess.move(movePoint3));
        assertTrue(testPrincess.getPosition().equals(movePoint3));

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
        Princess testPrincess = new Princess(true, testPoint);
        assertTrue(testPrincess.getPosition().equals(testPoint));

        Point movePoint = new Point(6, 3);
        assertTrue(testPrincess.move(movePoint));
        Point testPoint2 = new Point(6,3);
        assertTrue(testPrincess.getPosition().equals(testPoint2));

        Point illegalMovePoint = new Point(5, 20);
        assertFalse(testPrincess.move(illegalMovePoint));
        assertTrue(testPrincess.getPosition().equals(testPoint2));

        System.out.println("Passed getPosition() testing");
    }

}