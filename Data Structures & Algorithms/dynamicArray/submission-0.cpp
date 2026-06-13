class DynamicArray {
int capacity;
int size;
int* buf;
public:

    DynamicArray(int capacity) 
    : capacity{capacity},
    size{0},
     buf{new int[capacity]}{

    }

    int get(int i) {
        return buf[i];
    }

    void set(int i, int n) {
        buf[i]=n;
    }

    void pushback(int n) {
        if(size==capacity)
            resize();
        buf[size++] = n;
    }

    int popback() {
        --size;
        return buf[size];
    }

    void resize() {
        int* new_buf = new int[capacity *2];
        for(int i=0;i<size;++i){
           new_buf[i]=buf[i];
        }
        delete[] buf;
        buf=new_buf;
        capacity*=2;
    }

    int getSize() {
        return size;

    }

    int getCapacity() {
        return capacity;
    }
    ~DynamicArray(){
    delete[] buf;}
};
