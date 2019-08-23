package test;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import excercise_1.AND;
import excercise_1.NAND;
import excercise_1.OR;
import excercise_1.Perceptron;
public class Perceptron1_Test {
	private Perceptron p1,p2,p3;
	private int out;
	@Before
	public void setUp() throws Exception {
		p1 = new AND(5,3);
		p2 = new OR(7,-2);
		p3 = new NAND(3,9);
		}

	@Test
	public void test() {
		out = p1.exec(0,1);
		assertEquals(0,out);
		
		out = p2.exec(1, 0);
		assertEquals(1,out);
		
		out = p3.exec(1, 1);
		assertEquals(0,out);
		}

	}
