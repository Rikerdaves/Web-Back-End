const baseUrl = 'http://127.0.0.1:8000/tasks';

let Works = [];
let work_id
let editing = false;

function resetar_formulario() {
    const form_task = document.getElementById('form-task')
    form_task.reset()

    const btn_confirmar = document.getElementById('btn-Enviar')
    btn_confirmar.value = 'Adicionar Tarefa'

    editing = false
}

function atualizar_tela(){
    // Manipulacao de DOM
    const ul_tarefas = document.getElementById('list-tarefas')
    ul_tarefas.innerHTML = []

    for(let work of Works){
        const item = document.createElement('li')

        const label = `#${work.id} - ${work.descricao} -  ${work.responsavel} - ${work.nivel} - 
        ${work.prioridade} - ${work.situacao}  `
        

        item.innerText = label

        ul_tarefas.appendChild(item)
    }
}

function preencher_formulario(work){
    const form_task = document.getElementById('form-task')

    const inputs = form_task.children
    inputs[0].value = work.descricao
    inputs[1].value = work.responsavel
    inputs[2].value = work.nivel
    inputs[3].value = work.prioridade
    inputs[4].value = work.situacao
}

async function carregar_tarefas(){
    console.log('API - Todas as tarefas')
    const response = await fetch(baseUrl)

    const status = response.status
    Works = await response.json()

    atualizar_tela()
}

function configurar_formulario(){
    const form_task = document.getElementById('form-task')



    form_task.onsubmit = async function(event){

        event.preventDefault()

        const nivel = document.getElementById('nivel').value
        const prioridade = document.getElementById('prioridade').value
        const situacao = document.getElementById('situacao').value

        const dados = form_task.children
        const descricao = dados[0].value
        const responsavel = dados[1].value
        const select_nivel = Number(nivel)
        const select_prioridade = Number(prioridade)
        const select_situacao = Number(situacao)

        const  tarefa = {descricao, responsavel, select_nivel, select_prioridade, select_situacao}

        console.log('Submeteu!!!')

        let url = baseUrl
        let method = 'POST'
        let mensagem_ok = 'Tarefa adicionada com sucesso!'
        let mensagem_erro = 'Não foi possível adicionar'
        let response_status = 201

        const opcoes = {
            method: method, 
            body: JSON.stringify(tarefa),
            headers: {
                'Content-Type': 'application/json'
            }
        }

        const response = await fetch(url, opcoes)
    
        if (response.status === response_status ){
            alert(mensagem_ok)
            carregar_tarefas()
            resetar_formulario()
        }else{
            alert(mensagem_erro)
        }
        
    }
}

function app(){
    console.log('API Tarefas iniciada')
    configurar_formulario()
    carregar_tarefas()
}

app()