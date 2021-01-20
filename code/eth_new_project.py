from web3 import Web3

def main():
    #入手した自分のURLに差し替えて下さい．
    infura_url = "https://mainnet.infura.io/v3/YOUR_URL_HERE"

    #次のようにWeb3接続をインスタス化
    web3 = Web3(Web3.HTTPProvider(infura_url))

    #次のように接続されていることを確認できます．
    print(web3.isConnected())

    #コピーしたアドレスを変数に格納します．
    address = "0x063E3CA65C9F3bF3a63d373e6b2A6Db76f6d6263"

    #次のように残金を入手します
    balance = web3.eth.getBalance(address)

    #単位を変換します
    balance = web3.fromWei(balance, 'ether')
    print(balance)

if __name__ == "__main__":
    main()