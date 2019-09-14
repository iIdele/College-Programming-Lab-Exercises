import java.util.ArrayList;
public class Truck
{
	int engineSize;
	public Truck(int engineSize)
	{
		this.engineSize = engineSize;
	}

	public String toString()
	{
		return "Engine Size:"+engineSize;
	}

	public <T extends Comparable> int compareTo(T engineSize1, T engineSize2)
	{
		int indicator = 0;
		if(engineSize1 > engineSize2)
		{
			indicator = 1;
		}
		else if (engineSize1 < engineSize2)
		{
			indicator = -1;
		}
		return indicator;
	}

	public static void main(String [] args)
	{
		Truck ford = new Truck(2500);
		Truck chevy = new Truck(1500);
		Truck nissan = new Truck(2000);
		Truck vw = new Truck(1340);
		Truck mercedes = new Truck(2200);
		
		System.out.println(ford.compareTo(ford.engineSize, chevy.engineSize));
	}
}