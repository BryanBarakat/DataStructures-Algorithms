import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static class Program{
        private int[] arr = new int[6];

        private void askMarks(){
            int counter = 0;
            int fail_count = 0;
            int pass_count = 0;
            int twoByTwo = 0;
            int twoByOne = 0;
            int first_count = 0;
            while(counter < 6){
                System.out.println(String.format("Choose your grade number %s",counter+1));
                Scanner scanner = new Scanner(System.in);
                int inp = scanner.nextInt();
                if(inp < 40){
                    fail_count++;
                }
                else if (inp >= 40 && inp <= 49){
                    pass_count++;
                }
                else if(inp >= 50 && inp <= 59){
                    twoByTwo++;
                }
                else if(inp >= 60 && inp <= 69){
                    twoByOne++;
                }
                else if(inp >= 70){
                    first_count++;
                }
                arr[counter] = inp;
                counter++;
            }
            System.out.println(Arrays.toString(arr));
            System.out.println(String.format("Fail: %d // Pass: %d // 2:2: %d // 2:1: %d // First: %d",fail_count,pass_count,twoByTwo,twoByOne,first_count));
        }

        public double avg(){
            int total = 0;
            for(int i = 0;i<arr.length;i++){
                total += arr[i];
            }
            return (total / arr.length);
        }

        public void max(){
            int max = 0;
            for (int i : arr){
                if(i > max){
                    max = i;
                }
            }
            System.out.println(String.format("maximum grade is: %d" ,max));
        }

        public void min(){
            int min = arr[arr.length-1];
            for (int i : arr){
                if(i < min){
                    min = i;
                }
            }
            System.out.println(String.format("minimum grade is: %d" ,min));
        }

        public int[] sort(){
            for(int i = 0;i<arr.length;i++){
                for(int j = 0;j<arr.length-1;j++){
                    if(arr[j] > arr[j+1]){
                        int temp = arr[j + 1];
                        arr[j+1] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
            return arr;
        }

    }

    public static void main(String[] args){
//        var prog = new Program();
//        prog.askMarks();
//        System.out.println(prog.avg());
//        prog.max();
//        prog.min();
//        System.out.println(Arrays.toString(prog.sort()));
        var queue = new Queue();
        queue.Queue(5);
        queue.enqueue(50);
        queue.enqueue(80);
        queue.enqueue(70);
        queue.enqueue(65);
        queue.enqueue(12);
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
        System.out.println(queue);
    }

}
