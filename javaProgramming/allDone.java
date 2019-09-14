public class allDone
{
	static boolean alldone(String word, String guesses)
	{
		int correct = 0;
		for(int i=0; i<word.length(); i++)
		{
			for(int j=0; j< guesses.length(); j++)
			{
				if (word.charAt(i) == guesses.charAt(j)) 
				{
					correct = correct + 1;
				}
			}
		}

		return correct == word.length();
	}

	public static void main(String [] args)
	{
		System.out.println(alldone("computer", "putxmocre"));
		System.out.println(alldone("computer", "xcomp"));
	}
}