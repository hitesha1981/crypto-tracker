# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-29 05:01 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 12.48% | $57,706,756 | $0.0086 |
| 2 | trump | 9.67% | $1,159,759,638 | $3.0000 |
| 3 | ub | 7.76% | $13,438,095 | $0.1400 |
| 4 | npc | 7.42% | $7,843,037 | $0.0179 |
| 5 | ohm | 4.64% | $1,169,688 | $18.8400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ansem | -13.80% | $14,549,845 | $0.3299 |
| 2 | dog | -11.64% | $1,355,639 | $0.0012 |
| 3 | btse | -11.41% | $4,137,095 | $0.7086 |
| 4 | cashcat | -10.11% | $37,198,377 | $0.1859 |
| 5 | vvv | -9.19% | $23,463,997 | $15.9500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $57,389,144,233 | $1.0000 |
| 2 | btc | -2.49% | $31,551,013,050 | $77,647.0000 |
| 3 | usdc | 0.00% | $16,554,793,697 | $1.0000 |
| 4 | eth | -1.81% | $13,544,667,460 | $2,440.2900 |
| 5 | sol | -2.67% | $5,372,084,666 | $103.8800 |


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
