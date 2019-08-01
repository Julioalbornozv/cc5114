package tarea_1;

public abstract class Perceptron {
	protected int bias;
	protected int w1, w2;
	
	public Perceptron(int weight1, int weight2) {
		this.w1 = weight1;
		this.w2 = weight2;
		det_bias();
		}
	
	public int exec(int x, int y) {
		if (x*w1+y*w2+bias > 0) {
			return 1;
			}
		else {
			return 0;
			}
		}
	
	protected abstract void det_bias();
	}
