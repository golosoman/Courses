$(document).ready(() => {
    $("#content").html("<h1>Привет TypeScript</h1>");
});

$(() => {
    $("#alertBtn").click((e) => { $("#content").html("<h2>Привет мир</h2>"); });
});