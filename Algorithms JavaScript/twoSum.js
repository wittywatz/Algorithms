const twoSum = (arr,target) =>{
  const map = {};
  for(let i=0; i<arr.length; i++){
    let currentVal = map[arr[i]]
    if(currentVal !== undefined){
      return [currentVal, i]
    }
    let value = target - arr[i]
    map[value]=i
  }
  return null
}

//Both solutions work same
const twoSum= (arr,target) =>{
  const map = {};
  for(let i=0; i<arr.length; i++){
   let value = target - arr[i];
    if (value in map){
      return [map[value], i]
    }
    map[arr[i]]=i
  }
  return null
}


twoSum([1,3,7,9,2],4)

