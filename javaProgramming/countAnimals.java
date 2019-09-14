import java.util.*;
class countAnimals
{
	public static LinkedHashMap<String, Integer> tally(LinkedHashMap<String, Integer> m, Scanner in)
	{
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
		return m;
	}
	public static void main(String [] args)
	{
		LinkedHashMap<String, Integer> animals = new LinkedHashMap<String, Integer>();
		System.out.println("Enter some animals: ");

		Scanner in = new Scanner(System.in);

		System.out.println(tally(animals, in));
	}
}