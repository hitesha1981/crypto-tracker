# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-30 02:40 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | tac | 168.58% | $59,888,840 | $0.0594 |
| 2 | re | 28.31% | $2,690,514,396 | $0.7317 |
| 3 | ub | 24.03% | $36,522,447 | $0.1054 |
| 4 | h | 21.34% | $28,419,141 | $0.0730 |
| 5 | cx | 18.97% | $1,635,313 | $0.0939 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | -17.70% | $59,358,035 | $1.6100 |
| 2 | skyai | -14.63% | $38,993,111 | $0.1194 |
| 3 | jto | -12.31% | $61,161,176 | $0.7253 |
| 4 | slx | -9.43% | $169,330,265 | $0.5155 |
| 5 | btse | -8.66% | $2,486,520 | $0.7938 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $53,751,851,498 | $0.9986 |
| 2 | btc | 0.47% | $30,801,719,186 | $59,922.0000 |
| 3 | usdc | 0.00% | $15,741,430,359 | $0.9997 |
| 4 | eth | 1.05% | $11,491,213,412 | $1,589.6900 |
| 5 | sol | 3.52% | $4,019,790,995 | $74.2000 |


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
