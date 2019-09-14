import java.util.Scanner;

public class printFive
{
	public static void main(String [] args)
	{
		Scanner in = new Scanner(System.in);

		System.out.println("Enter five numbers:");
		String nums = in.next();
		
		System.out.println(nums);
	}
}