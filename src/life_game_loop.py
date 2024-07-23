import numpy as np
import matplotlib.pyplot as plt

class LifeGameLoop:
    def __init__(self, size, probabilities):
        self.size = size
        self.probabilities = probabilities
        self.current_state = self._initialize_automaton(size, probabilities)
        self.state_list = []

    def _initialize_automaton(self, size, probabilities):
        """セルオートマトンの初期状態をランダムに生成"""
        assert sum(probabilities) == 1, "Probabilities must sum to 1"
        assert len(probabilities) == 2, "Length of probabilities must match cnt_states"
        return np.random.choice(2, size=(size, size), p=probabilities)

    def _is_frozen(self):
        """全体が周期性、つまり凍結相になったか確認する"""
        current_state = self.current_state.copy()
        self.state_list.append(current_state)

        if len(self.state_list) < 2:
            return False

        slow_ptr, fast_ptr = 0, 1

        while fast_ptr < len(self.state_list):
            if np.array_equal(self.state_list[slow_ptr], self.state_list[fast_ptr]):
                return True
            slow_ptr += 1
            fast_ptr += 2

        max_states = 2
        if len(self.state_list) > max_states:
            self.state_list.pop(0)

        return False

    def _update_generation(self):
        """次の世代の状態を二重ループで計算"""
        new_state = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                total = sum([self.current_state[(i-1)%self.size][(j-1)%self.size],
                             self.current_state[(i-1)%self.size][j],
                             self.current_state[(i-1)%self.size][(j+1)%self.size],
                             self.current_state[i][(j-1)%self.size],
                             self.current_state[i][(j+1)%self.size],
                             self.current_state[(i+1)%self.size][(j-1)%self.size],
                             self.current_state[(i+1)%self.size][j],
                             self.current_state[(i+1)%self.size][(j+1)%self.size]])

                if self.current_state[i][j] == 1:
                    if total == 2 or total == 3:
                        new_state[i][j] = 1
                    else:
                        new_state[i][j] = 0
                else:
                    if total == 3:
                        new_state[i][j] = 1
                    else:
                        new_state[i][j] = 0

        self.current_state = new_state

    def _plot_current_state(self, img, ax, step, is_frozen):
        """現在の状態をプロット"""
        img.set_data(self.current_state)
        ax.set_title(f"Step: {step}")
        print(f"\r Current Step: {step+1}, Frozen: {is_frozen}", end="")
        plt.draw()
        plt.pause(0.01)

    def run(self, max_t, from_showing_graph=0):
        """実行関数"""
        plt.ion()
        fig, ax = plt.subplots()
        img = ax.imshow(self.current_state, cmap='binary')
        plt.show()
        is_frozen = False
        for t in range(1,max_t):
            self._update_generation()
            is_frozen = self._is_frozen()
            if t > from_showing_graph:
                self._plot_current_state(img, ax, t, is_frozen)
            if is_frozen:
                break
        print("")
        plt.ioff()
        plt.close()
        return is_frozen, t

def main():
    size = 150
    max_t = 100
    probabilities = [0.5, 0.5]
    from_showing_graph = 0

    game = LifeGameLoop(size, probabilities)
    is_frozen, t = game.run(max_t, from_showing_graph)
    print(f"Simulation ended at step {t} with frozen state: {is_frozen}")

if __name__ == "__main__":
    main()
