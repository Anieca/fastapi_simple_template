fastapi-simple-template
===
FastAPI を用いた簡素な Web サーバーを構築する際のテンプレートです

## features

### Poetry
パッケージ管理ツールに Poetry を採用し、各種設定ファイルを pyproject.toml に集約しています

### pre-commit
pre-commit を利用し、ローカルでのコミット直前に linter と formatter を実行します

### Docker
Docker を用いてテスト用のイメージ、本番環境用のイメージを作成します

コンテナを用いることでテスト時の環境差異を減らすことができます

また、GitHub Actions, Circle CI 等のサービスにイメージを持ち込むことでサービス内でのテストが容易に実現できます

本番環境用のイメージをクラウドベンダーの提供するコンテナレジストリに登録することでクラウド環境へのデプロイが容易に実現できます
