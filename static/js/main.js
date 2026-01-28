function like(id){
 fetch(`/like/${id}`,{method:"POST"})
 .then(r=>r.json())
 .then(d=>{
   document.getElementById(`like-${id}`).innerText=d.likes
 })
}

function enviarComentario(id){
 let input=document.getElementById(`coment-${id}`)
 let texto=input.value

 if(texto.length<3) return

 fetch("/comentario",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({
    atividade_id:id,
    texto:texto
  })
 })
 .then(r=>r.json())
 .then(d=>{
   let area=document.getElementById(`lista-${id}`)
   area.innerHTML+=`<p>${d.data} - ${d.texto}</p>`
   input.value=""
 })
}
