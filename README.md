# メモリを監視

[![test](https://github.com/RiM72J/memory_monitoring/actions/workflows/test.yml/badge.svg)](https://github.com/RiM72J/memory_monitoring/actions/workflows/test.yml)

- システム内で最もメモリを消費しているプロセスを特定し、その情報をトピックとして送信・ログ出力するROS 2パッケージです。

## 概要
* **監視機能:** 3秒ごとにシステム全体のメモリ使用状況をスキャンします。
* **特定機能:** その時点で最もメモリ使用率が高いプロセスの名前と使用率を抽出します。
* **通信機能:** `/memory_usage` トピックへ情報を配信します。
* **警告機能:** 使用率が50%を超えた場合、ログレベルをWARNに引き上げて警告します。
## 実行環境
* Ubuntu 24.04 LTS
* ROS 2 Jazzy Jalisco
* Python 3.12
## 必要なライブラリ / 必要なパッケージ
* **psutil:** メモリ情報の取得に使用します。
```
$ sudo apt update
$ sudo apt install python3-psutil
```


## 使用方法
- 以下のコマンドを実行して、監視ノードを起動します。
```
$source install/setup.bash
$ ros2 launch memory_monitoring memory_monitoring.launch.py
```
- 実行すると、以下のように3秒ごとにメモリ最大消費プロセスがログ出力されます。
- **注意**: WSL環境では、WSL内部のLinuxプロセスのみが監視対象となります。
```
[listener-2] [INFO] [1766840290.322437984] [memory_listener]: Normal: talker (0.9%)
[listener-2] [INFO] [1766840293.314037117] [memory_listener]: Normal: code   (10.1%)

```
- メモリ使用率が50%を超えると、以下のように警告（WARN）が表示されます。
```
[listener-2] [WARN] [1766840305.314365824] [memory_listener]: High Memory Alert! stress (52.3%)
```
- 別の端末で以下のコマンドを実行すると、トピックとして配信されているデータも確認できます。
```
$ ros2 topic echo /memory_usage
data: 'Normal: talker: 0.9%'
---
data: 'Normal: code: 10.1%'
---
data: 'Warn: stress: 52.3%'
---
```




## ライセンス
- このパッケージは、3-Clause BSD Licenseの下で公開されています。
- © 2025 Ryomu Inukai
 
