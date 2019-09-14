public class Test
{
	String [] l;

	public Test (String [] list)
	{
		l = list;
	}

	public void remove(String s)
	{
		String [] copyList; 
		copyList = new String [l.length - 1];

		int j = 0;
		for(int i = 0;i < l.length; i++)
		{
			if (! l[i].equals(s))
			{
				copyList[j] = l[i];
				j++;
			}
		}

		l = copyList;
	}

	public int length()
	{
		int sum = 0;
		for(int i = 0;i < l.length; i++)
		{
			sum++;
		}
		return sum;
	}
	

	public static void main(String [] args)
    {
    	String [] x = {"10","11","12","13"};
    	Test l = new Test(x);

    	l.remove("11");
    	String [] y;
    	y = new String [0];


    	System.out.println(l.length());
    	System.out.println(y.length);
    } 
}  
