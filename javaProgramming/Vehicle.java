public class Vehicle
{
	private int numWheels;
	private int numDoors;

	Vehicle(int numWheels, int numDoors) 
	{
		this.numWheels = numWheels;
		this.numDoors = numDoors;
	}

	public String toString()
	{
		return "Wheels : " + numWheels + "\nDoors : " + numDoors;
	}

	public int getWheels()
	{
		return numWheels;
	}

	public int getDoors()
	{
		return numDoors;
	}

	public void setWheels(int wheels)
	{
		numWheels = wheels;
	}

	public void setDoors(int doors)
	{
		numDoors = doors;
	}

	public static void main(String [] args)
	{

		class Car extends Vehicle
		{
			private String type;
			private String make;
			private int price;

			Car(String type, String make, int price, int numWheels, int numDoors)
			{
				super(numWheels, numDoors);
				this.type = type;
				this.make = make;
				this.price = price;
			}

			public String toString()
			{
				return super.toString() + "\n" + type + ":" + make + ", " + price;
			}
		}
	
		Car hatchback = new Car("Car", "Volkswagon Golf", 40000,4,3);
		hatchback.setDoors(5);
		System.out.println(hatchback);
	}
}