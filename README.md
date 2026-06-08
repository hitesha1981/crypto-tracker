# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-08 02:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | 51.26% | $73,664,146 | $3.5400 |
| 2 | siren | 50.27% | $150,147,470 | $1.2900 |
| 3 | rail | 28.24% | $1,036,228 | $3.1500 |
| 4 | drv | 18.34% | $990,797 | $0.1134 |
| 5 | jto | 17.37% | $84,032,675 | $0.6104 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | home | -41.96% | $88,164,670 | $0.0305 |
| 2 | skyai | -39.34% | $62,613,354 | $0.2173 |
| 3 | gwei | -15.72% | $27,243,415 | $0.1268 |
| 4 | lab | -14.00% | $40,315,955 | $12.3900 |
| 5 | eurs | -9.89% | $8,713 | $1.0970 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $58,889,269,855 | $0.9996 |
| 2 | btc | 2.68% | $38,047,470,904 | $63,072.0000 |
| 3 | eth | 5.83% | $16,630,973,320 | $1,683.1100 |
| 4 | usdc | -0.01% | $12,709,007,831 | $0.9997 |
| 5 | sol | 4.60% | $3,282,777,648 | $66.3200 |


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
