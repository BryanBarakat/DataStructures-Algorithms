public class Array2 {

    private int[] arr;
    private int value;

    public Array2(int value){
        this.value = value;
        arr = new int[value];
    }
    public void insert(int val){
        for(int i = 0;i < arr.length;i++){
            if(arr[i] == 0){
                arr[i] = val;
                return;
            }
        }
        int[] new_arr = new int[arr.length+1];
        new_arr[new_arr.length -1] = val;
        for(int j = 0;j<arr.length;j++){
            new_arr[j] = arr[j];
        }
        arr = new_arr;
    }

    public int removeAt(int index){
        int boundary = 0;
        if(index >= arr.length){
            return -1;
        }
        else{
            for(int i = 0;i < arr.length;i++){
                boundary++;
                if(i == index){
                    arr[i] = 0;
                    for(int j = boundary;j < arr.length -1;j++){
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                    }
                }
            }
        }
        return -1;
    }


    public void print(){
        for(int i = 0; i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
    }

    public int indexOf(int value){
        for(int i = 0;i < arr.length;i++){
            if(i == value){
                return arr[i];
            }
        }
        return -1;
    }

}
