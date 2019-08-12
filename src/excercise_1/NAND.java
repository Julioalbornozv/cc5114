package excercise_1;

public class NAND extends Perceptron{
	public NAND(int x, int y) {
		super(x,y);
		}

	@Override
	protected void det_bias() {
		this.bias = -this.w1-this.w2-1;
		}
	}


