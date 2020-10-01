package java_challenges.utilities;


import org.junit.Test;

import java.util.EmptyStackException;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class MultiBracketValidationTest {

    @Test public void testMultiBracketSimpleHappyPathTrue() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        System.out.println(mbv.multiBracketValidationWithString("{and}"));
        assertTrue("testing simpleHappyPath", mbv.multiBracketValidationWithString("{and}"));
    }
    @Test public void testMultiBracketComplicatedHappyPathTrue() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertTrue("testing simpleHappyPath", mbv.multiBracketValidationWithString("({and})"));
    }
    @Test public void testMultiBracketAnotherComplicatedHappyPathTrue() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertTrue("testing pass of complicated string", mbv.multiBracketValidationWithString("()[({and})]"));
    }
    @Test public void testMultiBracketSimpleHappyPathFalse() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertFalse("testing failure of simple string", mbv.multiBracketValidationWithString("{and})"));
    }
    @Test public void testMultiBracketComplicatedHappyPathFalse() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertFalse("testing failure of complicated string", mbv.multiBracketValidationWithString("({and})["));
    }
    @Test public void testMultiBracketAnotherComplicatedHappyPathFalse() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertFalse("testing failure of longer complicated string", mbv.multiBracketValidationWithString("()[chipmunks({and})][]{"));
    }
    @Test public void testMultiBracketEmptyString() throws EmptyStackException {
        MultiBracketValidation mbv = new MultiBracketValidation();
        assertFalse("testing failure of empty string", mbv.multiBracketValidationWithString(""));
    }
}
