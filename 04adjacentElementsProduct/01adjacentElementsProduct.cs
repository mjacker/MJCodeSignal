using System;

public class Program
{
    static public void Main()
    {
        int [] array = new int [] {1, 2, 3, 4, 5};
        foreach (int n in array){
            Console.WriteLine(n);
        }
        solution(array);
    }


    static int solution(int[] inputArray) {
        int max = inputArray[0] * inputArray[1];
        int product = 0;
        for (int i = 0; i< inputArray.Length - 1;i++){
            product = inputArray[i] * inputArray[i+1];
            if (max < product) max = product;
        }
        Console.WriteLine("max: {0}", max);
        return max;
    }
}
