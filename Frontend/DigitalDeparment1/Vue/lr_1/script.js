const boardSize = 10;
const gameBoard = document.getElementById("game-board");
const cells = [];

let snake = [{ x: 0, y: 0 }];
let food = { x: 5, y: 5 };
/**
 *  отвечает за направление движения змейки
 */
let direction = "right";
/**
 * отвечает за скорость движения змейки
 */
let speed = 800;

function initializeGameBoard() {
    for (let row = 0; row < boardSize; row++) {
        for (let col = 0; col < boardSize; col++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cells.push(cell);
            gameBoard.appendChild(cell);
        }
    }
}

function render() {
    cells.forEach((cell) => cell.classList.remove("snake", "food"));

    snake.forEach((segment) => {
        const index = segment.x + segment.y * boardSize;
        cells[index].classList.add("snake");
    });

    const foodIndex = food.x + food.y * boardSize;
    cells[foodIndex].classList.add("food");
}

function update() {
    const head = Object.assign({}, snake[0]);

    switch (direction) {
        case "up":
            head.y -= 1;
            break;
        case "down":
            head.y += 1;
            break;
        case "left":
            head.x -= 1;
            break;
        case "right":
            head.x += 1;
            break;
    }

    if (
        head.x < 0 ||
        head.x >= boardSize ||
        head.y < 0 ||
        head.y >= boardSize
    ) {
        resetGame();
        return;
    }

    if (isCollisionWithSelf(head)) {
        resetGame();
        return;
    }

    if (head.x === food.x && head.y === food.y) {
        snake.unshift(head);
        generateFood();
    } else {
        snake.pop();
        snake.unshift(head);
    }
}

function isCollisionWithSelf(head) {
    return snake
        .slice(1)
        .some((segment) => segment.x === head.x && segment.y === head.y);
}

function generateFood() {
    food = {
        x: Math.floor(Math.random() * boardSize),
        y: Math.floor(Math.random() * boardSize),
    };
}

function resetGame() {
    snake = [{ x: 0, y: 0 }];
    direction = "right";
    generateFood();
    updateScore(snake.length);
}

initializeGameBoard();

function gameLoop() {
    update();
    render();
    updateScore(snake.length);
    setTimeout(gameLoop, speed);
}

// TODO: добавить обработчик нажатия на клавиши
document.addEventListener("keydown", (e) => {
    // console.log(e.key);
    switch (e.key) {
        case "ArrowUp":
            direction = "up";
            break;
        case "ArrowDown":
            direction = "down";
            break;
        case "ArrowLeft":
            direction = "left";
            break;
        case "ArrowRight":
            direction = "right";
            break;
    }
});

// TODO: добавить обработчик нажатия клавиши R (сброс игры)
document.addEventListener("keydown", (e) => {
    // console.log(e.key.toLowerCase());
    if (e.key.toLowerCase() === "r") {
        resetGame();
    }
});

// TODO: добавить обработчики нажатия кнопок
function createController() {
    let buttons = [];
    for (let arrow of ["↑", "←", "→", "↓"]) {
        const button = document.createElement("input");
        button.setAttribute("type", "button");
        button.setAttribute("class", "button");
        button.setAttribute("value", arrow);
        buttons.push(button);
    }

    const buttonId = ["up", "left", "right", "down"];
    for (let index = 0; index < buttons.length; index++) {
        buttons[index].setAttribute("id", buttonId[index]);
    }

    const divButtons = document.createElement("div");
    divButtons.setAttribute("class", "buttons");

    const controller = document.getElementById("joystick");
    controller.appendChild(buttons[0]);
    controller.appendChild(divButtons);
    controller.appendChild(buttons[3]);

    const buttons_in_controller = controller.querySelector(".buttons");
    buttons_in_controller.appendChild(buttons[1]);
    buttons_in_controller.appendChild(buttons[2]);
}

createController();

document
    .getElementById("up")
    .addEventListener("click", () => (direction = "up"));
document
    .getElementById("down")
    .addEventListener("click", () => (direction = "down"));
document
    .getElementById("left")
    .addEventListener("click", () => (direction = "left"));
document
    .getElementById("right")
    .addEventListener("click", () => (direction = "right"));

// TODO: добавить возможность изменения скорости змейки
function changeSpeed() {
    // const label = document.createElement('label');
    // label.setAttribute('for', 'speed');
    // label.innerText = speed;

    const field = document.createElement("input");
    field.setAttribute("type", "number");
    field.setAttribute("class", "field");
    // field.setAttribute('min', '200');
    // field.setAttribute('max', '1400');
    field.setAttribute("name", "speed");
    field.setAttribute("value", speed);

    document.getElementById("speed").appendChild(field);
}
changeSpeed();

document
    .querySelector(".field")
    .addEventListener("change", (e) => (speed = e.target.value));

updateScore(snake.length);
gameLoop();

function updateScore(score) {
    document.getElementById("score").innerHTML = "Счет: " + score;
}
