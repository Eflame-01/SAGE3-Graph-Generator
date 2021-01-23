/**graph.js is used to help facilitate communication between the python code and 
 * the server.
*/

var file
var textarea
const reader = new FileReader()

function onSubmit(){
    reader.addEventListener('load', (e)=>{
        textarea.value = e.target.result
        data = e.target.result
    })
    reader.addEventListener('error', (e)=>{
        alert(e.target.error.name)
    })

    if(file){
        reader.readAsText(file)
    }
}