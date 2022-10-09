public class Stack {

    private int[] arr = new int[5];
    private int count = 0;

    public boolean isEmpty(){
        int counter = 0;
        for(int i = 0;i<arr.length;i++){
            if(arr[i] != 0){
                counter++;
            }
        }
        if(counter > 0){
            return false;
        }
        return true;
    }

    public int peek(){
        return arr[arr.length-1];
    }

    public void push(int value){
        int[] new_arr = new int[arr.length +1];
        if(isEmpty()){
            arr[0] = arr[value];
            return;
        }
        for(int i = arr.length-1;i<= 0;i--){
            if(arr[i] == 0){
                arr[i] = value;
                return;
            }
        }
        for(int j = 0;j < arr.length;j++){
            new_arr[j] = arr[j];
        }
        new_arr[new_arr.length-1] = value;
        arr = new_arr;
    }

    public int pop(){
        int[] new_arr = new int[arr.length -1];
        int popped_value = arr[arr.length-1];
        for(int j = 0;j < new_arr.length;j++){
            new_arr[j] = arr[j];
        }
        arr = new_arr;
        return popped_value;
    }

}
