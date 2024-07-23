import os
import numpy as np
import yaml
import shutil
from datetime import datetime
import time
from life_game_convolution import LifeGameConvolution
from life_game_loop import LifeGameLoop

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def run_convolution_simulation(size, max_t, probabilities,from_showing_graph):
    game = LifeGameConvolution(size, probabilities)
    start_time = time.time()
    is_frozen, t = game.run(max_t,from_showing_graph)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return is_frozen, t, elapsed_time

def run_loop_simulation(size, max_t, probabilities,from_showing_graph):
    game = LifeGameLoop(size, probabilities)
    start_time = time.time()
    is_frozen, t = game.run(max_t,from_showing_graph)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return is_frozen, t, elapsed_time

def save_simulation_results(output_dir, size, is_frozen_conv, t_conv, elapsed_time_conv, is_frozen_loop, t_loop, elapsed_time_loop):
    results = {
        "convolution": {
            "size":size,
            "is_frozen": is_frozen_conv,
            "steps": t_conv,
            "time_seconds": elapsed_time_conv
        },
        "loop": {
            "size":size,
            "is_frozen": is_frozen_loop,
            "steps": t_loop,
            "time_seconds": elapsed_time_loop
        }
    }
    result_file = os.path.join(output_dir, 'simulation_results.yaml')
    with open(result_file, 'w') as file:
        yaml.dump(results, file)

def main():
    # 設定ファイルを読み込む
    config = load_config()
    
    # 日付付きフォルダの作成
    current_date = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"{config['save_path']}_{current_date}"
    os.makedirs(output_dir, exist_ok=True)

    # 設定ファイルのコピー
    shutil.copy('config.yaml', os.path.join(output_dir, 'config.yaml'))

    size = config['size']
    max_t = config['max_t']
    probabilities = config['probabilities']
    from_showing_graph = config['from_showing_graph']

    # 畳み込みを使用したライフゲームのシミュレーション
    is_frozen_conv, t_conv, elapsed_time_conv = run_convolution_simulation(size, max_t, probabilities,from_showing_graph)
    print(f"Convolution Simulation[{size}x{size}] ended at step {t_conv} with frozen state: {is_frozen_conv} in {elapsed_time_conv:.4f} seconds")

    # 二重ループを使用したライフゲームのシミュレーション
    is_frozen_loop, t_loop, elapsed_time_loop = run_loop_simulation(size, max_t, probabilities,from_showing_graph)
    print(f"Loop Simulation[{size}x{size}] ended at step {t_loop} with frozen state: {is_frozen_loop} in {elapsed_time_loop:.4f} seconds")

    # 結果の保存
    save_simulation_results(output_dir,size, is_frozen_conv, t_conv, elapsed_time_conv, is_frozen_loop, t_loop, elapsed_time_loop)

if __name__ == "__main__":
    main()
