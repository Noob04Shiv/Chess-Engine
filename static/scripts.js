$(document).ready(function() {
    var board,
        game = new Chess();

    var makeMove = function() {
        var fen = game.fen();
        var depth = $('#depth-select').val();
        $.get('/move/' + depth + '/' + fen, function(move) {
            game.move(move, { sloppy: true });
            board.position(game.fen());
        });
    };

    var onDrop = function(source, target) {
        var move = game.move({
            from: source,
            to: target,
            promotion: 'q'
        });

        if (move === null) return 'snapback';

        makeMove();
    };

    var onSnapEnd = function() {
        board.position(game.fen());
    };

    var cfg = {
        draggable: true,
        position: 'start',
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
    };
    board = ChessBoard('board', cfg);

    $('#reset-button').on('click', function() {
        game.reset();
        board.position('start');
    });
});
