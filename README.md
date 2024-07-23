# conway-game-of-life-acceleration-with-convolution

このプロジェクトでは、コンウェイのライフゲームを畳み込みを用いて実装したものと、二重ループを用いて実装したもののパフォーマンスを比較します。  
目的は、両方の方法の計算効率を評価し、比較することです。

## 目次

- [インストール](#インストール)
- [使用方法](#使用方法)
- [設定](#設定)
- [結果](#結果)
- [ライセンス](#ライセンス)

## インストール

このプロジェクトを実行するには、Pythonがインストールされている必要があります。  
また、追加のパッケージも必要です。必要なパッケージはpipを使用してインストールできます。

```sh
pip install numpy scipy matplotlib pyyaml
```

## 使用方法

1. リポジトリをクローンします。

```sh
git clone https://github.com/yourusername/life-game-simulation.git
cd life-game-simulation
```

2. プロジェクトのルートディレクトリに`config.yaml`ファイルを作成します。以下の構造に従います。

```yaml
save_path: "simulation_results"
size: 150
max_t: 100
probabilities: [0.5, 0.5]
from_showing_graph: 0
```

3. メインスクリプトを実行して、シミュレーションを実行し、パフォーマンスを比較します。

```sh
python main.py
```

## 設定

`config.yaml`ファイルには、シミュレーションのパラメータが含まれています。  
これらのパラメータを調整することで、シミュレーションを自分のニーズに合わせることができます。

- `save_path`: 結果を保存するディレクトリ。
- `size`: グリッドのサイズ（例：150の場合、150x150グリッド）。
- `max_t`: シミュレーションする最大世代数。
- `probabilities`: セル状態の初期確率。
- `from_showing_graph`: グラフ表示を開始するステップ。

例 `config.yaml`:

```yaml
save_path: "simulation_results"
size: 150
max_t: 100
probabilities: [0.5, 0.5]
from_showing_graph: 0
```

## 結果

シミュレーションの結果（フリーズ状態かどうか、ステップ数、畳み込みとループの両方の実行時間）は、  
指定された`save_path`ディレクトリに`simulation_results.yaml`ファイルとして保存されます。

例 `simulation_results.yaml`:

```yaml
convolution:
  is_frozen: false
  size: 500
  steps: 99
  time_seconds: 0.6115050315856934
loop:
  is_frozen: false
  size: 500
  steps: 99
  time_seconds: 114.31272387504578
```

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は[LICENSE](LICENSE)ファイルを参照してください。
