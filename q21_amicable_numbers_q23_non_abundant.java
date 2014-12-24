/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package euler;

/**
 *
 * @author Ringo
 */
public class Euler {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //System.out.println(ProperDivisors(220));
        //System.out.println(ProperDivisors(284));
        //System.out.println(Amicable(10000));
        System.out.println(PerfectNumbers());
    }
    // q21
    public static int Amicable(int max){
        /*Let d(n) be defined as the sum of proper divisors of n (numbers less 
        than n which divide evenly into n). If d(a) = b and d(b) = a, where 
        a ≠ b, then a and b are an amicable pair and each of a and b are called
        amicable numbers. For example, the proper divisors of 220 are 
        1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
        The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
        Evaluate the sum of all the amicable numbers under 10000.*/
        int sum = 0;
        int amicable = 2;
        while (amicable < max){
            int friend = ProperDivisors(amicable);
            if (ProperDivisors(friend) == amicable && friend != amicable){
                System.out.printf("Pair: %d and %d\n", friend, amicable);
                if (friend < max){
                    sum += friend;
                }
                sum += amicable;
            }
            amicable++;
        }
        return sum/2;
    }
    //q23
    public static int PerfectNumbers(){
    /*A perfect number is a number for which the sum of its proper divisors is 
    exactly equal to the number. For example, the sum of the proper divisors of 
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
    A number n is called deficient if the sum of its proper divisors is less 
    than n and it is called abundant if this sum exceeds n.
    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
    number that can be written as the sum of two abundant numbers is 24. By 
    mathematical analysis, it can be shown that all integers greater than 28123 
    can be written as the sum of two abundant numbers. However, this upper limit
    cannot be reduced any further by analysis even though it is known that the 
    greatest number that cannot be expressed as the sum of two abundant numbers 
    is less than this limit.
    Find the sum of all the positive integers which cannot be written as the sum
    of two abundant numbers.*/
        int max = 20161;
        boolean[] Remaining = new boolean[max+1];
        // initialize all the numbers which can be written as sum of abundants 
        // to false
        for (int i=0;i<max+1;i++){
            Remaining[i] = false;
        }
        //get all the abundant numbers
        boolean[] Abundant = new boolean[max+1];
        Abundant[0] = false;
        for (int j=1;j<max+1;j++){
            if (ProperDivisors(j) > j){
                Abundant[j] = true;
                //System.out.printf("%d: True\n", j);
            }
            else{
                Abundant[j] = false;
                //System.out.printf("%d: False\n", j);
            }
        }
        // now set everything to true that can be written as sum of abundant 
        // numbers CAN INCLUDE THE SAME ABUNDANT # TWICE WTF
        for (int k=12;k<max+1;k++){
            if (Abundant[k] == true){
                for (int l=k;l<max+1;l++){
                    if (Abundant[l] == true){
                        if (l+k < max+1){
                            Remaining[l+k] = true;
                        }
                    }
                }
            }
        }
        for (int i=0;i<max+1;i++){
            if (Remaining[i] == true){
            }
            else{
                System.out.printf("%d: False\n", i);
            }
        }
        // now get sum from remaining
        int sum = 0;
        for (int i=1;i<max+1;i++){
            if (Remaining[i] == false){
                sum += i;
            }
        }
        return sum;
        
    }
    public static int ProperDivisors(int num){
        // returns sum of proper divisors of a number
        int sum = 1;
        int i = 2;
        while (i*i <= num){ // iterate till i is equal to square root of num
            if (num % i == 0){
                sum += i;
                if (i*i < num){
                    sum += num / i;            
                }
            }
            i++;
        }
        return sum;
    }
}
