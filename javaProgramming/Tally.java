import java.util.*;
import java.io.*;

public class Tally
{
	public static void main(String [] args) throws Exception
	{
		Map<String, Integer> m = new HashMap<String, Integer>();

		Scanner in = new Scanner(new File("text.txt"));

		String word = in.next();
		while (in.hasNext())
		{
			if (m.containsKey(word))
			{
				m.put(word, m.get(word) + 1);
			}
			else
			{
				m.put(word, 1);
			}

			word = in.next();
		}

		for (String key : m.keySet())
		{
			if (m.get(key) == 2)
			{
				System.out.println(key);
			}
		}
	}
}