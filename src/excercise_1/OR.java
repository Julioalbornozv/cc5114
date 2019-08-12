package excercise_1;

public class OR extends Perceptron {
	public OR(int x, int y) {
		super(x,y);
		}

	@Override
	protected void det_bias() {
		this.bias = 0;
		}
	}

