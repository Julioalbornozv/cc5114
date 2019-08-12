package test;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import excercise_2.Perceptron;
import java.util.Random;
import java.util.LinkedList;
import java.util.List;

public class Perceptron2_Test {
	private Perceptron p = new Perceptron();
	private Random seed = new Random();
	private List<Point> field = new LinkedList<>();
	
	private class Point{
		double x,y;
		public Point(double a,double b) {
			x = a;
			y = b;
			}	
		}
	private void gen_points(int n){
		for (int i = 0; i < n; i++) {
			double x = -50.0f + seed.nextDouble() * (50.0f + 50.0f);
			double y = -50.0f + seed.nextDouble() * (50.0f + 50.0f);
			field.add(new Point(x,y));
			}
		}
	
	@Before
	public void setUp() throws Exception {
		System.out.println("Generating points...");
		gen_points(100);
		}

	@Test
	public void test() {
		fail("Not yet implemented");
	}

}
