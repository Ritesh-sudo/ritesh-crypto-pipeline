import json, websocket, kafka, sys

# Optional while debugging
websocket.enableTrace(True)

producer = kafka.KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode(),
)

def on_msg(ws, msg):
    # --- debug print (leave as-is) -----------------------------------------
    print("WS payload:", msg[:120], file=sys.stderr)

    raw = json.loads(msg)               # ① parse Binance event

    # ② map raw keys → clean schema  (this is NEW)
    tick = {
        "symbol": raw["s"],                      # BTCUSDT
        "price":  float(raw["p"]),               # 109199.01
        "qty":    float(raw["q"]),               # 0.00021
        "side":   "BUY" if raw["m"] is False else "SELL",
        "ts":     raw["T"],                      # epoch-ms
    }

    # ─ debug: confirm we’re sending the mapped dict  (this is NEW)
    print("SENDING:", tick, file=sys.stderr)

    
    fut = producer.send("raw_ticks", tick)
    fut.add_errback(lambda exc: print("Kafka send error:", exc, file=sys.stderr))
    # producer.flush(0)   # <- comment or delete once you're happy

def on_err(ws, err):
    print("WS error:", err, file=sys.stderr)

ws = websocket.WebSocketApp(
    "wss://stream.binance.us:9443/ws/btcusdt@trade",
    on_message=on_msg,
    on_error=on_err,
)

ws.run_forever(ping_interval=20, ping_timeout=10)
