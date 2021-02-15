class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  } 
}

class LinkedList {
  constructor(){
    this.head = null;
    this.tail = this.head;
    this.length = 0;
  }
  append(value){
    const newNode = new Node(value)
    if (this.head === null){
      this.head = newNode
      this.tail = this.head
    }else{
      this.tail.next = newNode
      this.tail=newNode
    }
    this.length++
  }
  prepend(value){
    const newNode = new Node(value)
    if (this.head === null){
      this.head = newNode
      this.tail = this.head
    }else{
      newNode.next = this.head
      this.head=newNode
    }
    this.length++
  }
  insert(index,value){
    if(index >= this.length){
      //If index is out of range just append at the end
      return this.append(value) 
    }
    if(index < 0){
      return //Won't handle negative indexing.... 
      // check Python implementation for LinkedList
    }
    if (index === 0){
      //Just prepend
      this.prepend(value)
    }else if(index === this.length-1){
      //Just append
      this.append(value)
    }else{
      let currentnode = this.head
      let i = 0
      while (i < index-1){
        currentnode = currentnode.next
        i++
      }
      const newNode = new Node(value)
      newNode.next = currentnode.next
      currentnode.next = newNode
    }
  }
  
  pop(){
    if(this.length === 0){
      return
    }
    if(this.length === 1){
      this.head = null
      this.tail = null
    }else{
      let currentnode = this.head
      let i = 0
      while(i< this.length-2){
        currentnode = currentnode.next
        i++
      }
      currentnode.next = null
      this.tail = currentnode
    }
    this.length--
  };
  remove(index){
    if(index >= this.length){
      return
    }
    if(index < 0){
      return
    }
    if(index === this.head-1){
      return this.pop()
    }
    let currentnode = this.head
    let i = 0
    while(i<index-1){
      currentnode = currentnode.next
      i++
    }
    currentnode.next=currentnode.next.next
    this.length--
  }
  size(){
    return this.length
  }
  reverse(){
    let flag = true
    let nextnode = null
    let previousnode = null
    let currentnode = this.head
    while(currentnode){
      nextnode = currentnode.next
      currentnode.next = previousnode
      previousnode = currentnode
      currentnode = nextnode
      if(flag){
        this.tail = previousnode
        flag = false
      }
    }
    this.head = previousnode  
  }
  printListItems(){
    const array = [];
    let currentnode = this.head;
    while(currentnode !== null){
      array.push(currentnode.value)
      currentnode = currentnode.next
    }
    return array
  }
}
const myLinkedList = new LinkedList;
// myLinkedList.append(5);
// myLinkedList.append(16);
// myLinkedList.prepend(1);
// // myLinkedList.printListItems();
// // myLinkedList.insert(2,99)
// myLinkedList.reverse()
// // myLinkedList.printListItems();

// console.log(myLinkedList.head.next.value)
