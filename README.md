##　メモリを監視

[![ROS 2 CI](https://github.com/RiM72J/memory_monitoring/actions/workflows/test.yml/badge.svg)](https://github.com/RiM72J/memory_monitoring/actions/workflows/test.yml)

- システム内で最もメモリを消費しているプロセスを特定し、その情報をトピックとして送信・ログ出力するROS 2パッケージです。

## 概要
* **監視機能:** 3秒ごとにシステム全体のメモリ使用状況をスキャンします。
* **特定機能:** その時点で最もメモリ使用率が高いプロセスの名前と使用率を抽出します。
* **通信機能:** `/memory_usage` トピックへ情報を配信します。
* **警告機能:** 使用率が50%を超えた場合、ログレベルをWARNに引き上げて警告します。
**注意:** WSL環境では、WSL内部のLinuxプロセスのみが監視対象となります。
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
## セットアップ
 ```
$cd ~/ros2_ws/src$ git clone https://github.com/RiM72J/memory_monitoring.git
 ```


## 使用方法





## ライセンス
- このパッケージは、BSD-3-Clause Licenseの下で公開されています。
-　© 2025　Ryomu　Inukai
 
