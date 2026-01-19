# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-19 01:15 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 33.14% | $58,603,787 | $27.1700 |
| 2 | dash | 9.54% | $778,095,198 | $79.5100 |
| 3 | ip | 7.82% | $291,389,889 | $2.6800 |
| 4 | h | 7.76% | $34,836,192 | $0.1952 |
| 5 | xmr | 7.15% | $376,935,171 | $612.0500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | gala | -14.07% | $71,785,166 | $0.0067 |
| 2 | mana | -13.97% | $91,158,446 | $0.1456 |
| 3 | theta | -13.45% | $27,518,441 | $0.3093 |
| 4 | fet | -12.67% | $84,441,417 | $0.2420 |
| 5 | wape | -12.59% | $632,686 | $0.1987 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $60,938,295,041 | $0.9996 |
| 2 | btc | -2.27% | $32,262,021,031 | $92,733.0000 |
| 3 | eth | -2.57% | $21,456,722,080 | $3,214.9100 |
| 4 | sol | -5.99% | $4,774,249,055 | $134.1100 |
| 5 | usdc | -0.78% | $4,580,850,640 | $0.9998 |


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
