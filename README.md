# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-26 01:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 39.17% | $27,998,282 | $2.3900 |
| 2 | siren | 25.46% | $84,858,307 | $2.2100 |
| 3 | mon | 15.56% | $112,520,095 | $0.0269 |
| 4 | ath | 15.16% | $51,418,579 | $0.0079 |
| 5 | ena | 14.72% | $189,441,466 | $0.1088 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -8.65% | $23,576,983 | $21.6500 |
| 2 | tibbir | -6.16% | $1,124,873 | $0.1227 |
| 3 | night | -6.06% | $1,186,306,558 | $0.0448 |
| 4 | b | -5.20% | $3,139,048 | $0.2064 |
| 5 | zro | -5.01% | $48,025,694 | $2.1400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $61,277,481,692 | $0.9996 |
| 2 | btc | 0.68% | $36,002,614,388 | $71,231.0000 |
| 3 | eth | 0.17% | $16,386,686,388 | $2,164.0300 |
| 4 | usdc | -0.01% | $7,342,309,192 | $0.9998 |
| 5 | sol | 0.68% | $3,450,290,326 | $91.7900 |


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
