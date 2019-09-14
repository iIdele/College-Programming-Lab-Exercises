public class movieHelp
{
	String sentence;
	private int number;

	public movieHelp(String s, int n)
	{
		 sentence = s;
		 number = n;
	}

	public void helper()
	{
		int hello = 6;
	}

	public static void main(String [] args)
	{	
		movieHelp help = new movieHelp("This is the first sentence", 1);
		System.out.println(helper().hello);
    }
}