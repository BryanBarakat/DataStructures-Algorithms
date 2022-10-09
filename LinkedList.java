public class LinkedList {


    private class Node {
        private int data;
        private Node next;

        public Node(int data){
            this.data = data;
        }
    }
    private Node head;
    private Node tail;

    public void addFirst(int value){
        Node new_node = new Node(value);
        if(head == null){
            head = tail = new_node;
        }
        else{
            new_node.next = head;
            head = new_node;
        }
    }

    public void addLast(int value){
        var new_node = new Node(value);
        if(head == null){
            head = tail = new_node;
        }
        else{
            tail.next = new_node;
            tail = new_node;
        }
    }

    public int size(){
        Node curr = head;
        int counter = 0;
        if(curr.next == null){
            return 0;
        }
        while(curr.next != null){
            counter++;
            curr = curr.next;
        }
        return counter;
    }

    public boolean isEmpty(){
        return head.next == null;
    }

    public void deleteFirst(){
        if(isEmpty()){
            throw new IndexOutOfBoundsException();
        }
        else if(head == tail){
            head = tail = null;
        }
        else{
            Node temp = head.next;
            head.next = null;
            head = temp;
        }
    }

    public void deleteLast(){
        Node curr = head;
        if (isEmpty()) {
            throw new IndexOutOfBoundsException();
        }
        else if(head == tail){
            head = tail = null;
        }
        else{
            while(curr.next != null){
                curr = curr.next;
                if(curr.next == null){
                    curr = null;
                }
            }
        }
    }

    public boolean contains(int value){
        Node curr = head;
        while(curr != null){
            curr = curr.next;
            if(curr.data == value){
                return true;
            }
        }
        return false;
    }

    public int indexOf(int value){
        Node curr = head;
        int index = 0;
        while(curr != null){
            if(curr.data == value){
                return index;
            }
            index++;
            curr = curr.next;
        }
        return -1;
    }

}
