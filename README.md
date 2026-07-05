# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-05 02:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lab | 169.74% | $144,232,413 | $16.2400 |
| 2 | velvet | 24.16% | $40,025,840 | $0.5758 |
| 3 | h | 17.21% | $20,223,788 | $0.0818 |
| 4 | ethfi | 13.60% | $89,243,148 | $0.4210 |
| 5 | nex | 11.56% | $19,372,707 | $0.0000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | -10.65% | $16,002,588 | $1.3900 |
| 2 | b | -9.52% | $7,779,875 | $0.2134 |
| 3 | grass | -7.26% | $27,438,349 | $0.5169 |
| 4 | bp | -7.03% | $2,746,556 | $0.5409 |
| 5 | hash | -6.94% | $2,444 | $0.0087 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $33,397,650,962 | $0.9991 |
| 2 | btc | 0.47% | $17,820,496,156 | $62,698.0000 |
| 3 | eth | 0.87% | $7,941,990,421 | $1,760.9100 |
| 4 | usdc | -0.01% | $6,452,707,491 | $0.9998 |
| 5 | sol | -1.75% | $2,056,602,106 | $80.5000 |


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
