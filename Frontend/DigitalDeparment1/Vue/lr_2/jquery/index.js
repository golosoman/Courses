const tasks = [];

function addTask() {
    const newTask = $("#new-task").val();
    if (newTask.trim() !== "") {
        tasks.push({ text: newTask, completed: false });
        const listItem = $('<li class="todo-item"></li>');
        const taskText = $("<span></span>").text(newTask);
        $(listItem).append(taskText);

        // Контейнер для кнопок
        const buttonsContainer = $("<div><div>", {
            class: "buttonsContainer",
        });
        $(listItem).append(buttonsContainer);

        // Добавление кнопки для изменения записи, а также слушателя события
        const buttonUpdate = $("<button></button>", {
            class: "update",
            text: "✏",
        });
        $(buttonUpdate).on("click", (e) => {
            e.stopPropagation();
            const text = prompt("Введите текст записи:");
            $(taskText).text(text);
        });
        $(buttonsContainer).append(buttonUpdate);

        // Добавление кнопки для удаления записи, а также слушателя события
        const buttonDelete = $("<button></button>", {
            class: "delete",
            text: "❌",
        });
        $(buttonDelete).on("click", (e) => {
            e.stopPropagation();
            $(listItem).remove();
        });
        $(buttonsContainer).append(buttonDelete);

        $(listItem).on("click", function () {
            const index = $(this).index();
            tasks[index].completed = !tasks[index].completed;
            $(this).toggleClass("completed");
        });

        $("#todo-list").append(listItem);
        $("#new-task").val("");
    }
}

$("form").on("submit", function (e) {
    e.preventDefault();
    addTask();
});
