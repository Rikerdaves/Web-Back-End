const baseUrl = 'https://tarefasapi-u4ir.onrender.com/document/';

let Works = [];

document.getElementById("form-task").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário
  
    // Obtém os valores dos campos do formulário
    const descricao = document.getElementsByName("descricao")[0].value;
    const responsavel = document.getElementsByName("responsavel")[0].value;
    const nivel = document.getElementsByName("nivel")[0].value;
    const prioridade = document.getElementsByName("prioridade")[0].value;
    const situacao = document.getElementsByName("situacao")[0].value;

  
    // Envia os dados para a lista no FastAPI usando uma solicitação HTTP POST
    fetch(baseUrl, {
      method: "POST",
      body: JSON.stringify({ descricao, responsavel, nivel, prioridade, situacao }),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => {
      // Verifica se a resposta foi bem-sucedida
      if (response.ok) {
        console.log("Tarefas enviadas com sucesso!");
      } else {
        console.error("Erro ao enviar:", response.status);
      }
    })
    .catch(error => {
      console.error("Erro ao enviar:", error);
    });
});

function atualizar_tela(){
  // Manipulacao de DOM
  const ul_tarefas = document.getElementById('list')
  ul_tarefas.innerHTML = []

  for(let work of Works){
    const item = document.createElement('li')

    const label = `ID: ${work.id} - Descrição: ${work.descricao} -  Responsável: ${work.responsavel} - 
                    Nível: ${work.nivel} - Prioridade: ${work.prioridade} - Situação: ${work.situacao}`
      
    item.innerText = label

    ul_tarefas.appendChild(item)
  }
}

async function carregar_tarefas(){
  console.log('Lista - Todos as Tarefas OK')
  const response = await fetch(baseUrl, { mode: 'cors' })

  const status = response.status
  Works = await response.json()

  atualizar_tela()
}

async function atualizar_tarefa(){
  console.log('Atualizar - Tarefa atualizada OK')
  
}

console.log('API Tarefas iniciada!');
carregar_tarefas();