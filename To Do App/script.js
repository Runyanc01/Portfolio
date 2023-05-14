let todos = [];

const todosList = document.getElementById("todos");
const todoInput = document.getElementById("textInput");
const inputButton = document.getElementById("add");
const showEnterTodo = document.getElementById("showEnterTodo");
const enterTodo = document.getElementById("enterTodo");

function showTodoInput () {
    enterTodo.style.display = "block";
};

showEnterTodo.addEventListener("click", showTodoInput);


function addTodo(e) {
    e.preventDefault();
    let textValue = todoInput.value;
    todos.push(textValue);
    todosList.innerHTML = '';
    renderTodos();
    todoInput.value = '';
    enterTodo.style.display = "none";
};
inputButton.addEventListener("click", addTodo);


function removeTodo(index) {
    todos = todos.filter((todo, i) => {
        return i == index ? false : true;
    });
    todosList.innerHTML = '';
    renderTodos();
};


function editTodo(index) {
    const currElement = document.querySelector(`#todos div:nth-child(${index + 1}) p`).innerHTML;
    const splicedText = currElement.slice(3);
    
    removeTodo(index);
    showTodoInput();
    todoInput.value = splicedText;
};


function renderTodos() {
    let newHTML = '';
    todos.forEach((todo, i) => {
        newHTML += `<div class="todoItem">
                        <p>${i + 1}. ${todo}</p>
                        <div class="actions">
                        <i onclick="editTodo(${i})" class="fa-solid fa-pen"></i>
                            <i onclick="removeTodo(${i})" class="fa-regular fa-trash-can"></i>
                        </div>
                    </div>`;
    });
    todosList.innerHTML = newHTML;
};

window.onload = renderTodos;