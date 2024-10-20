const tasks = [];

function addTask() {
    const newTask = document.getElementById("new-task").value;
    if (newTask.trim() !== "") {
        tasks.push({ task: newTask, completed: false });
        const taskIndex = tasks.length - 1;

        const listItem = document.createElement("li");
        listItem.className = "todo-item";
        const taskNameElement = document.createElement("span");
        taskNameElement.innerText = newTask;
        listItem.appendChild(taskNameElement);

        // Контейнер для кнопок
        const buttonsContainer = document.createElement("div");
        buttonsContainer.className = "buttonsContainer";
        listItem.appendChild(buttonsContainer);

        // Добавление кнопки для изменения записи, а также слушателя события
        const updateButton = document.createElement("button");
        updateButton.className = "update";
        updateButton.textContent = "✏";
        updateButton.addEventListener("click", (e) => {
            e.stopPropagation();
            const text = prompt("Введите текст записи:");
            taskNameElement.innerText = text;
        });
        buttonsContainer.appendChild(updateButton);

        // Добавление кнопки для удаления записи, а также слушателя события
        const deleteButton = document.createElement("button");
        deleteButton.className = "delete";
        deleteButton.textContent = "❌";
        deleteButton.addEventListener("click", () => {
            // e.stopPropagation();
            listItem.parentNode.removeChild(listItem);
        });
        buttonsContainer.appendChild(deleteButton);

        listItem.addEventListener("click", function (e) {
            e.stopPropagation();
            tasks[taskIndex].completed = !tasks[taskIndex].completed;
            taskNameElement.classList.toggle("completed");
        });

        document.getElementById("todo-list").appendChild(listItem);
        document.getElementById("new-task").value = "";
    }
}

document.getElementById("add-button").onclick = addTask;
