public class Mean
{
	static double mean(int [] l)
	{
		double total = 0;
		for(int i = 0; i<l.length; i++)
		{
			total = total + l[i];
		}

		return total / l.length;
	}

	public static void main(String [] args)
	{

		int [] l = {2,3,5,7,11,13,17};
		System.out.println(mean(l));
	}
}