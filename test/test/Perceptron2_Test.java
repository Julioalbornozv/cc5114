package test;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import excercise_2.Perceptron;
import java.util.Random;


public class Perceptron2_Test {
	private Perceptron p = new Perceptron();
	private Random seed = new Random();
	
	private double gen_point(){
		return -50.0f + seed.nextDouble() * (50.0f + 50.0f);
		}
	
	@Before
	public void setUp() throws Exception {
		
		}

	@Test
	public void test() {
		fail("Not yet implemented");
	}

}
