let inputs= document.getElementById("task");
let text= document.querySelector(".text");

function Add(){
    if(inputs.value == ""){
        alert("please enter the task")
    }
    else{
        let newelement= document.createElement("ul");
        newelement.innerHTML=`${inputs.values}`;

        text.appendChild(newelement)
        inputs.value=""
    }


}