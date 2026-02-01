# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-01 01:45 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zk | 5.41% | $52,859,166 | $0.0257 |
| 2 | kag | 3.72% | $2,949,458 | $92.5400 |
| 3 | rain | 3.37% | $27,780,673 | $0.0097 |
| 4 | hype | 2.44% | $767,335,049 | $31.9500 |
| 5 | kau | 2.32% | $262,457 | $161.2100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -29.07% | $41,141,955 | $24.9400 |
| 2 | ip | -17.18% | $80,027,844 | $1.4400 |
| 3 | sent | -16.72% | $685,164,157 | $0.0368 |
| 4 | hash | -15.32% | $27,235 | $0.0214 |
| 5 | wlfi | -14.48% | $188,041,143 | $0.1308 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.05% | $143,236,394,837 | $0.9990 |
| 2 | btc | -6.67% | $80,310,410,010 | $78,323.0000 |
| 3 | eth | -9.87% | $49,499,125,200 | $2,434.2100 |
| 4 | sol | -11.51% | $10,311,998,915 | $104.2900 |
| 5 | usdc | -0.00% | $9,691,445,551 | $0.9996 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key

[coingecko-api-key-docs](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)

## Requirements to setup
## 1. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 2. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add pandas requests matplotlib python-dotenv
```


---

## 4. Update coingecko demo key in .env ( I have provided in .env.sample)
```bash
cat .env
CGK_API_DEMO_KEY="Your-coingecko-demo-api-key-here"
```

---

## 3. To manually run the script
```bash
python3.12 main.py
```
---
