public class reverseList
{
	public static int [] reverse(int [] list)
	{
		int end = list.length - 1;

		for(int i = 0; i < end/2; i++)
		{
			int tmp = list[i];
			list[i] = list[end - i];
			list[end - i] = tmp;
		}
		return list;
	}

	public static void main(String[] args){
		int [] l = {1,2,3,4,5,6};
		l = reverse(l);
		for(int i = 0; i < l.length; i++)
		{
			System.out.println(l[i]);
		}
	}
}