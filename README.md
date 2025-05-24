# Valorant Combat Trainer

An interactive text-based Python game inspired by **Valorant**. Players manage an agent’s condition, choose weapons, and battle opponents with varying difficulty. This project focuses on decision-making, resource management, and simple combat simulation.

---

## 🎮 Features

- Agent status management: Energy, Skill, and Mental State
- Weapon selection: Vandal, Phantom, and Operator, each with unique stats
- Opponent selection: Bot, Bronze, Platinum, and Radiant
- Strategic combat outcomes based on stats and randomness
- Manual choices for both weapons and enemies
- Game ends when any agent attribute reaches 0

---

## 🧠 How It Works

1. The agent starts with default stats.
2. Each turn, the player can:
   - Enter a battle (choose weapon and enemy)
   - Rest to recover energy and mental state
3. Battle outcome is based on:
   - Agent's skill, mental state, weapon stats
   - Enemy difficulty and fatigue factor (energy)
   - Random variation to simulate unpredictability
4. After each action, the agent's condition changes.
5. The game ends when the agent burns out (any stat ≤ 0).

---

## 🛠️ Requirements

- Python 3.x  
- No external libraries required

---
