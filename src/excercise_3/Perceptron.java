package excercise_3;

import java.util.Random;
import java.lang.Math;
public class Perceptron {
	protected double bias;
	protected double w1, w2;
	protected Random seed = new Random();
	protected double lr = 0.1f; //Learning rate
	
	public Perceptron() {
		w1 = gen_number();
		w2 = gen_number();
		bias = gen_number();
		}
	
	private double gen_number(){
		return -2.0f + seed.nextDouble() * (2.0f + 2.0f);
		}
	
	public void exec(int x, int y, int desired) {
		double out = 1/(1+Math.exp(-w1*x+-w2*y-bias));
		double diff = desired - out;
		w1 += (lr * x * diff);
		w2 += (lr * y * diff);
		bias += (lr * diff);
		}
	
	}

