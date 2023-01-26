fastapi-simple-template
===
FastAPI を用いた簡素な Web サーバーを構築する際のテンプレートです

## features

### Poetry
パッケージ管理ツールに Poetry を採用することで、各種設定ファイルを pyproject.toml に集約しています

### Pre-Commit
pre-commit を利用することでローカルでのコミット直前に linter, formatter が実行されます

### Docker
Docker を用いてテスト用のイメージ、本番環境用のイメージを作成できます

テスト用のイメージを用いることで CI が実現できます
本番環境用のイメージをクラウドベンダーの提供するコンテナレジストリに登録することでクラウド環境へのデプロイが実現できます

### CI(not yet)
github actions を用いた CI が可能です

pre-commit はローカルで実現していましたが CI でも実行します
また、前述のテストイメージを GitHub Actions にデプロイし、テストを行います

### gunicorn, uvicorn

### dependency injection container
代表的なソフトウェアエンジニアリングのプラクティスである Dependency Injection を実現します

DI Container に集約させることで見通しの良い実装が実現できます

テストにおいても DI Container の機能を用いてサービスをモックで上書きすることで、シンプルにモックを用いた単体テストを書くことが出来ます
