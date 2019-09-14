import java.util.ArrayList;

public class arrayList
{
	public static void main(String [] args)
	{
		int n = 10;

		ArrayList<Integer> nums = new ArrayList<Integer>();
		nums.add(1);
		nums.add(2);
		nums.add(3);

		// for (int i = 0; i <= n; i++)
		// {
		// 	nums.add(i);
		// }
		System.out.println(nums.size());
	}
}