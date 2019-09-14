public class Student
{
	String name;
	int mark;

	public Student(String name, int mark)
	{
		this.name = name;
		this.mark= mark;
	}

	public String toString()
	{
		return "Name: " + name + "\nMark: " + mark;
	}

	public String getName()
	{
		return name;
	}

	public int getMark()
	{
		return mark;
	}

	public void setName(String newName)
	{
		name = newName;
	}

	public void setMark(int newMark)
	{
		mark = newMark;
	}

	public static void main(String [] args)
	{
		Student student = new Student("John", 100);
		System.out.println(student);
		student.setName("Conor");
		System.out.println(student);

	}
}