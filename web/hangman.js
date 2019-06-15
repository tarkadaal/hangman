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
        var lives_left = document.getElementById("lives_left");
        var status = document.getElementById("status");
        var button = document.getElementById("guess");
        var score = document.getElementById("score");
        var high_score = document.getElementById("high_score");
        known.innerHTML = data.printable_known;
        lives_left.innerHTML = "Lives left: " + data.lives_left;
        high_score_label = data.is_new_high_score ? "NEW HIGH SCORE: " : "High score: "
        high_score.innerHTML = high_score_label + data.high_score;
        if(data.is_finished){
            if (data.was_last_guess_correct == true) {
                status.innerHTML = "YOU WIN!";
            }
            if (data.was_last_guess_correct == false) {
                status.innerHTML = "GAME OVER :(";
            }
            button.style.visibility = "collapse";
            score.innerHTML = "You scored: " + data.score;
        }
        else {
            if (data.was_last_guess_correct == true) {
                status.innerHTML = "Good guess!";
            }
            if (data.was_last_guess_correct == false) {
                status.innerHTML = "Bad guess!";
            }
        };

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
