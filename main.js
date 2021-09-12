mybutton  = document.getElementById("button1");
mybutton2 = document.getElementById("button2");

mybutton.onclick = function(){
    var k = document.getElementById("cname").value;
    alert(k + " course added sucessfuly");
    mydiv = document.getElementById("test");
    mydiv.append(k);
};

// mybutton2.onclick = function(){
//     var i;
//     for(i=0 ; i<6 ;i++){
        
//     }
   
// }




