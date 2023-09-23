# collect-license

pipインストールされたパッケージのライセンスファイルを収集するモジュールです。
pip-licensesを使用します。

## 動作確認OS

- `Windows 11 Pro`

## インストール方法

``` cmd or bash
pip install collectlicense
```

## 実行方法

``` cmd or bash
python -m collectlicense --out .licenses --clear
```

## ソースから実行する方法

``` cmd
git clone https://github.com/hamacom2004jp/collect-license.git
cd collect-license
python -m venv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python -m collectlicense
deactivate
```

