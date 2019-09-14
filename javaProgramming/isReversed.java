public class isReversed
{
	public static boolean isReversed(int [] l1, int [] l2)
	{
		boolean bool = true;
		int end = l1.length - 1;

		for(int i = 0; i <= end; i++)
		{
			if (l1[i] != l2[end - i])
			{
				bool = false;
				break;
			}
		}

		return bool;
	}

	public static void main(String[] args){
		int [] l = {1,2,3,4,5,6};
		int [] r = {6,5,4,2,2,1};
		System.out.println(isReversed(l,r));
	}
}