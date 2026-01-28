# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-28 01:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 58.08% | $81,600,304 | $0.4778 |
| 2 | khype | 26.43% | $20,621,298 | $32.1600 |
| 3 | hype | 26.09% | $709,726,223 | $31.8000 |
| 4 | whype | 25.97% | $185,094,420 | $31.8100 |
| 5 | pump | 21.61% | $475,763,510 | $0.0033 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | jst | -12.35% | $46,595,245 | $0.0409 |
| 2 | river | -12.26% | $93,257,866 | $70.7900 |
| 3 | sun | -8.06% | $69,892,315 | $0.0174 |
| 4 | axs | -6.71% | $441,761,382 | $2.4800 |
| 5 | sand | -4.86% | $43,770,441 | $0.1273 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $79,840,669,071 | $0.9987 |
| 2 | btc | 1.31% | $44,217,695,811 | $89,301.0000 |
| 3 | eth | 3.62% | $28,749,360,110 | $3,017.7200 |
| 4 | usdc | -0.00% | $23,705,727,413 | $0.9997 |
| 5 | paxg | 2.90% | $10,008,474,386 | $5,196.1300 |


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
