(function(){
    var base_url = 'http://192.168.1.42:5000/';
    var start_request;
    var start_game_url = base_url + 'hangman/api/start_game';
    var take_turn_url = base_url + 'hangman/api/take_turn';
    var current_data;

    function guess_button_handler() {
        var data = current_data;
        data.guess = window.prompt("What's your guess?");
        var xhr = new XMLHttpRequest();
        xhr.open("POST", take_turn_url, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = on_take_turn;
        xhr.send(JSON.stringify(data));
    }

    function play(data){
        var known = document.getElementById("current_known");
        known.innerHTML = data.printable_known;
        var lives_left = document.getElementById("lives_left");
        lives_left.innerHTML= "Lives left: " + data.lives_left;
    }


    function on_take_turn(){
        var data = current_data = JSON.parse(this.response);
        play(data);
    }

    function on_game_started(){
        var button = document.getElementById("guess");
        button.addEventListener("click", guess_button_handler);
        var data = current_data = JSON.parse(this.response);
        play(data);
    }

    function main() {
        start_request = new XMLHttpRequest();
        start_request.open('GET', start_game_url);
        start_request.onload = on_game_started;
        start_request.send();
    }

    main();
}());
