# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-16 02:42 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 78.47% | $89,789,169 | $0.0284 |
| 2 | blorb | 73.62% | $2,310,694 | $0.1131 |
| 3 | 龙虾 | 29.49% | $28,361,810 | $0.2000 |
| 4 | arb | 14.25% | $447,858,823 | $0.1534 |
| 5 | useless | 10.08% | $38,881,150 | $0.2225 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stonk | -21.14% | $34,725,400 | $0.1553 |
| 2 | npc | -13.27% | $8,002,352 | $0.0194 |
| 3 | inj | -11.36% | $112,310,182 | $5.4500 |
| 4 | dcr | -11.23% | $2,645,910 | $14.9000 |
| 5 | jup | -10.92% | $65,486,401 | $0.2140 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $68,926,747,617 | $0.9994 |
| 2 | btc | -2.39% | $39,983,122,719 | $75,972.0000 |
| 3 | usdc | -0.02% | $20,094,818,704 | $0.9997 |
| 4 | eth | -4.17% | $19,288,934,897 | $2,406.9300 |
| 5 | xrp | -9.24% | $5,854,702,144 | $1.2900 |


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
