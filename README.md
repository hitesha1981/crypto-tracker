# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-26 02:40 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | 27.50% | $46,111,497 | $2.2400 |
| 2 | data | 23.08% | $132,617,271 | $0.4027 |
| 3 | skyai | 20.53% | $33,379,638 | $0.3095 |
| 4 | awe | 16.55% | $7,201,624 | $0.0686 |
| 5 | tac | 16.14% | $1,474,934 | $0.0237 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | -19.47% | $9,863,039 | $0.3015 |
| 2 | bp | -17.18% | $4,654,508 | $0.5095 |
| 3 | mnt | -15.17% | $61,680,984 | $0.4251 |
| 4 | apyusd | -12.03% | $8,337,230 | $0.9914 |
| 5 | apxusd | -11.71% | $14,682,275 | $0.7306 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $65,837,017,795 | $0.9985 |
| 2 | btc | -3.32% | $42,104,706,268 | $58,683.0000 |
| 3 | usdc | -0.01% | $17,171,872,136 | $0.9997 |
| 4 | eth | -5.05% | $15,900,966,749 | $1,532.2300 |
| 5 | sol | -1.91% | $3,612,574,274 | $66.4400 |


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
