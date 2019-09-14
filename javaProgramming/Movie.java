import java.util.Scanner;

public class Movie 
{
    public static final int CHILDRENS = 2;
    public static final int REGULAR = 0;
    public static final int NEW_RELEASE = 1;
    
    private String _title;
    private int _priceCode;
    
    public Movie(String title, int priceCode) 
    {
        _title = title;
        _priceCode = priceCode;
    }
    public int getPriceCode() 
    {
        return _priceCode;
    }
    public void setPriceCode(int arg) 
    {
        _priceCode = arg;
    }
    public String getTitle ()
    {
        return _title;
    };

    public double getCharge(int daysRented)
    {
        double charge = 0;
        switch (getPriceCode())
        {
            case Movie.REGULAR:
                charge += 2;
                if (daysRented > 2)
                    charge += (daysRented - 2) * 1.5;
                break; 
        
            case Movie.NEW_RELEASE:
                charge += daysRented * 3;
                break;

            case Movie.CHILDRENS:
                charge += 1.5;
                if (daysRented > 3)
                    charge += (daysRented - 3) * 1.5;
                break; 
        }
        return charge;
    }

    public int getFrequentRenterPoints(int numDays)
    {
        int points = 0;
        points++;
        if ((getPriceCode() == Movie.NEW_RELEASE) && numDays > 1)
            points++;
        return points;
    }
}