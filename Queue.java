import java.util.Arrays;

public class Queue {

    private int[] arr;

    private int front = 0;
    private int rear = 0;

    private int count = 0;

    public void Queue(int cap){
        this.arr = new int[cap];
    }

    public boolean isEmpty(){
        return rear == 0;
    }

    public boolean isFull(){
        return rear == arr.length;
    }

    public int peek(){
        return arr[front];
    }

    public void enqueue(int value){
        if(isFull()){
            throw new StackOverflowError();
        }
        else{
            arr[rear++] = value;
            count++;
        }
    }

    public void dequeue(){
        if(isEmpty()){
            throw new RuntimeException();
        }
        else{
            arr[front++] = 0;
            count--;
            sort();
        }
    }

    private void sort(){
        int counter = 0;
        for(int i = front;i<arr.length;i++){
            arr[counter] = arr[i];
            arr[i] = 0;
            counter++;
        }
        rear = counter -1;
        front = 0;
        count = counter;
    }

    @Override
    public String toString(){
        return Arrays.toString(arr);
    }

}
