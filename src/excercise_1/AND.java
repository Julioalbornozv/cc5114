package excercise_1;

public class AND extends Perceptron {
	public AND(int x, int y) {
		super(x,y);
		}

	@Override
	protected void det_bias() {
		this.bias = -this.w1-this.w2+1;
		}
}
