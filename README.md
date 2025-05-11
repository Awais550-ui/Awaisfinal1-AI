# ♟️ CheckMate AI: Crafting a Smarter Chess Opponent

> **Under the guidance of**: Prof. Shivanjali Khare

---

## 🎯 Objective

CheckMate AI is designed to deliver a strategic and challenging chess experience by integrating both traditional and modern AI techniques. The game allows human players to compete against a computer-powered opponent that uses **Alpha-Beta Pruning** and **A3C (Asynchronous Advantage Actor-Critic)** reinforcement learning to make intelligent moves.

---

## 🧠 How the Game Works

CheckMate AI is a two-player chess game played on an 8x8 board. The human player competes against an AI that evaluates and decides moves based on board position, search algorithms, and learned policies. The objective is to **checkmate the opponent's king** while protecting your own.

---

## 🛠️ Requirements

- **Python**: Version 3.10 or higher  
- **Libraries**:
  - `pygame` – for GUI and board rendering
  - `time` – to measure AI decision-making speed

---

## 📁 Project Files

| File/Folder           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `assets/`             | Contains chess piece graphics                                               |
| `chess.py`            | Main script to launch the game                                              |
| `board.py`            | Defines the board and Alpha-Beta logic                                      |
| `pieces.py`           | Contains base class `Piece` and individual piece movement logic             |
| `ratings.py`          | Rates possible moves using heuristics                                       |
| `userInterface.py`    | Handles Pygame-based UI and player interactions                             |

---

## ♜ How Chess Pieces Move

- **King**: One square in any direction  
- **Queen**: Any number of squares in any direction  
- **Rook**: Horizontally or vertically  
- **Bishop**: Diagonally (same color)  
- **Knight**: L-shaped move (can jump over pieces)  
- **Pawn**: Forward one square (two if first move), captures diagonally, can promote

---

## 🤖 AI Algorithms

### ✅ Alpha-Beta Pruning

- **Purpose**: Optimizes Minimax by pruning unnecessary branches
- **Technique**:
  - `Alpha`: Best guaranteed score for maximizer
  - `Beta`: Best guaranteed score for minimizer
  - Skips evaluation of branches where `beta ≤ alpha`
- **Performance**: Default search depth is 3 (can be increased in `board.py`)

### ✅ A3C (Asynchronous Advantage Actor-Critic)

- **Purpose**: Reinforcement learning model for policy optimization
- **Technique**:
  - Runs multiple agents in parallel self-play environments
  - Learns board evaluations (value function) and move strategies (policy function)
- **Outcome**: Adaptive learning over time, improved decision-making accuracy

---

## 🧪 Evaluation Metrics

- **AI Decision Time**: Measured in real-time (mostly < 1 second per move)
- **Move Validation**: Each piece follows legal movement rules
- **Adaptability**: A3C improves over time via self-play training
- **Depth Testing**: Change `self.MAXDEPTH` in `board.py` to evaluate performance impact

---

## 📦 Deliverables

- ✅ Fully playable Chess AI Game
- ✅ Source code repository hosted on GitHub
- ✅ Detailed documentation on setup and algorithms
- ✅ Project demo video

---

## 🎮 How to Play

1. Clone or download the project repository
2. Ensure all required libraries are installed (e.g., `pip install pygame`)
3. Run the game:
   ```bash
   python chess.py
