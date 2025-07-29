import unittest
from chess_engine import Engine

class TestChessEngine(unittest.TestCase):

    def test_initialization(self):
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        engine = Engine(fen)
        self.assertEqual(engine.board.fen(), fen)

    def test_material_eval(self):
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        engine = Engine(fen)
        self.assertEqual(engine.material_eval(), 0)

        fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
        engine = Engine(fen)
        self.assertEqual(engine.material_eval(), 0)

    def test_iterative_deepening(self):
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        engine = Engine(fen)
        move = engine.iterative_deepening(1)
        self.assertIn(move, [str(m) for m in engine.board.legal_moves])

if __name__ == '__main__':
    unittest.main()
