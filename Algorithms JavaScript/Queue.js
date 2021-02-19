//Code goes here

class Queue{
  constructor(){
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  peek(){
    return this.head && this.head.value
  }
  enqueue(value){
    const newNode = new Node(value)
    if(this.head === null){
      this.head = newNode
      this.tail= this.head
    }else{
      this.tail.next = newNode
      this.tail = newNode
    }
    this.length++
  }
  dequeue(){
    if(this.length === 0){
      return null
    }
    if (this.length === 1){
      this.head = null
      this.tail = null
      return
    }
    this.head = this.head.next
    this.length--
  }
  isEmpty(){
    return this.head === null;
  }
  printQueueItems(){
    const array = [];
    let currentnode = this.head;
    while(currentnode !== null){
      array.push(currentnode.value)
      currentnode = currentnode.next
    }
    return array
  }
}
const myQueue = new Queue;
