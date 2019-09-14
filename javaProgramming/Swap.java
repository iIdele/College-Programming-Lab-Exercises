public class Swap
{
    public static <T> T [] swap(T [] list, int a, int b)
    {
        T tmp = list[a];
        list[a] = list[b];
        list[b] = tmp;
        
        return list;
        
    }

    public static void main(String [] args)
    {
        Integer [] l = {1,2,3};

        l = swap(l,0,1);

        for(int i=0; i < l.length; i++)
        {
            System.out.println(l[i]);
        }
    }

}   

