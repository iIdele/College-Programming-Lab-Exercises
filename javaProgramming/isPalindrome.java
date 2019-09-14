public class isPalindrome
{
	public static boolean palindrome(String s)
	{
		String reverse = "";
		for (int i = s.length()-1; i >= 0; i--)
		{
			reverse = reverse + s.charAt(i);
		}
		return s.equals(reverse);
	}

	public static void main(String [] args)
	{
		String s = "madam";
		System.out.println(palindrome(s));
	}
}