class BinaryNode{
  constructor(value){
    this.left = null;
    this.right = null;
    this.value = value;
  }
}
class BinarySearchTree{
  constructor(){
    this.root = null
  }
  insert(value){
    const newNode = new BinaryNode(value)
    if (!this.root){
      this.root = newNode;
      return this;
    }
    const currentNode = this.root
    while(true){
      if(value < currentNode.value){
        //Go left
        if(!currentNode.left){
          currentNode.left = newNode
          return this
        }
        currentNode = currentNode.left
      }else{
        //go right for equal or greater than
        if(!currentNode.right){
          currentNode.right = newNode
          return this
        }
        currentNode = currentNode.right
      }
    }

  }
  lookup(value){
    if(!this.root){
      return null
    }
    const currentNode = this.root
    while(true){
      if(value < currentNode.value){
        //Go left
        if(!currentNode.left){
          return null
        }
        currentNode = currentNode.left
      }else{
        if (value === currentNode.value){
          return currentNode
        }
        if (!currentNode.right){
          return null
        }
        currentNode = currentNode.right
      }
    }
  }
  remove(){

  }

}
const myBST = new BinarySearchTree
