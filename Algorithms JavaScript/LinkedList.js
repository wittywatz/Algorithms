class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  } 
}

class LinkedList {
  constructor(value){
    this.head = new Node(value)
    this.tail = this.head;
    this.length = 1
  }
  append = (value) => {
    const newNode = new Node(value)
    this.tail.next = newNode
    this.tail=newNode
    this.length++
    return this
  }
  prepend = (value) => {
    const newNode = new Node(value)

    newNode.next = this.head
    this.head=newNode
    this.length++
    return this
  }
  printListItems=()=>{
    const array = [];
    let currentnode = this.head;
    while(currentnode !== null){
      array.push(currentnode.value)
      currentnode = currentnode.next
    }
    return array
  }
  // insert = (index,value) => {

  // }
}
const myLinkedList = new LinkedList(10);
myLinkedList.append(2);
myLinkedList.append(9);
myLinkedList.prepend(4);
myLinkedList.prepend(6);
myLinkedList.prepend(7);
myLinkedList.prepend(8);
myLinkedList.prepend(9);
myLinkedList.prepend(10);
myLinkedList.printListItems();
// console.log(myLinkedList)
