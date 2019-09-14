import java.util.ArrayList;
public class BankAccount
{
	private double balance;
	public BankAccount(double b)
	{
		this.balance = b;
 	}

 	public double getBalance() 
 	{ 
 		return balance; 
 	}

 	public static int negativeBalance(ArrayList<BankAccount> balances)
 		{
 			int count = 0;
 			for(int i = 0; i<balances.size(); i++)
 			{
 				if (balances.get(i).getBalance() < 0)
 				{
 					count ++;
 				}
 			}
 			return count;
 		}

 	public static void main(String [] args)
 	{
 		BankAccount one = new BankAccount(2000);
 		BankAccount two = new BankAccount(-1000);
 		BankAccount three = new BankAccount(22000);
 		BankAccount four = new BankAccount(-2100);

 		ArrayList<BankAccount> l = new ArrayList<BankAccount>();
 		l.add(one);
 		l.add(two);
 		l.add(three);
 		l.add(four);

 		System.out.println(negativeBalance(l));

 	}
}
