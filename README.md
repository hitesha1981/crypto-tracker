# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-11 02:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 108.87% | $60,196,416 | $0.7809 |
| 2 | beat | 47.74% | $230,728,211 | $7.0300 |
| 3 | nex | 12.60% | $7,195,690 | $0.0000 |
| 4 | xmr | 10.94% | $135,384,943 | $340.5600 |
| 5 | crv | 10.68% | $81,086,821 | $0.2250 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | -24.33% | $20,407,567 | $0.6608 |
| 2 | btw | -20.82% | $37,086,944 | $0.0752 |
| 3 | b | -13.52% | $14,427,163 | $0.2223 |
| 4 | lab | -13.27% | $30,553,228 | $7.8100 |
| 5 | vvv | -12.35% | $53,085,693 | $13.0700 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $48,158,120,990 | $0.9989 |
| 2 | btc | 1.29% | $28,614,402,637 | $62,001.0000 |
| 3 | usdc | 0.01% | $13,388,527,009 | $0.9998 |
| 4 | eth | 0.75% | $12,290,323,940 | $1,633.3700 |
| 5 | sol | 0.18% | $3,162,451,728 | $64.3500 |


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
