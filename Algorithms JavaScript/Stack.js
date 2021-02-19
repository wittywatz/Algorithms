class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  } 
}

class Stack{
  constructor(){
    this.head = null; //Top of stack
    this.tail = this.head; //Bottom of stack
    this.length = 0;
  }
  top(){
    if (!this.top){
      return null;
    }
    return this.head && this.head.value
  }
  pop(){
    if (this.length===0){
      return
    }
    if(this.head===this.tail){
      this.tail = null
      this.head = null
    }else{
      this.head = this.head.next
    }
    this.length--
  }
  push(value){
    const newNode = new Node(value)
    if(this.head === null){
      this.head = newNode
      this.tail = this.head
    }else{
      newNode.next = this.head
      this.head = newNode
    }
    
    this.length++
  }
  size(){
    return this.length
  }
  isEmpty(){
    return this.head===null
  }
  printStackItems(){
    const array = [];
    let currentnode = this.head;
    while(currentnode !== null){
      array.push(currentnode.value)
      currentnode = currentnode.next
    }
    return array
  }
}

const myStack = new Stack
