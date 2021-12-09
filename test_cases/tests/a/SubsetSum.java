import java.util.*;
/*
 * Date 09/23/2014
 * @author Tushar Roy
 *
 * Given an array of non negative numbers and a total, is there subset of numbers in this array which adds up
 * to given total. Another variation is given an array is it possible to split it up into 2 equal
 * sum partitions. Partition need not be equal sized. Just equal sum.
 *
 * Time complexity - O(input.size * total_sum)
 * Space complexity - O(input.size*total_sum)
 *
 * Youtube video - https://youtu.be/s6FhG--P7z0
 */
public class SubsetSum {

    public boolean subsetSum(int input[], int total) {

        boolean T[][] = new boolean[input.length + 1][total + 1];
        for (int i = 0; i <= input.length; i++) {
            T[i][0] = true;
        }

        for (int i = 1; i <= input.length; i++) {
            for (int j = 1; j <= total; j++) {
                if (j - input[i - 1] >= 0) {
                    T[i][j] = T[i - 1][j] || T[i - 1][j - input[i - 1]];
                } else {
                    T[i][j] = T[i-1][j];
                }
            }
        }
        return T[input.length][total];

    }

    public static void main(String args[]) {
        SubsetSum ss = new SubsetSum();

        int arr1[] = {2, 3, 7, 8};
        System.out.print(ss.subsetSum(arr1, 11));

        int firstNum, secondNum, result;
        ArrayList<Integer[]> inp = new ArrayList<>();
        Scanner s = new Scanner(System.in);
        while(s.hasNextLine()){
            Integer[] boxed = Stream.of(s.nextLine().split(" ")).map(Integer::valueOf).toArray(Integer[]::new);
            inp.add(boxed);
        }

        System.out.println(inp);

    }
}