package excercise_2;

import java.util.Random;
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
		int out = 1;
		if (x*w1+y*w2+bias < 0.0f) { // Below line
			out = 0;
			}
		int diff = desired - out;
		
		//TODO: Generalize for n weights
		w1 += (lr * x * diff);
		w2 += (lr * y * diff);
		bias += (lr * diff);
		}
	
	}
