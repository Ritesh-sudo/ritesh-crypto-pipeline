import json, websocket, kafka, sys

# Optional while debugging
websocket.enableTrace(True)

producer = kafka.KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode(),
)

def on_msg(ws, msg):           # ← keep only 2 parameters
    print("WS payload:", msg[:120], file=sys.stderr)

    tick = json.loads(msg)
    fut = producer.send("raw_ticks", tick)
    fut.add_errback(lambda exc: print("Kafka send error:", exc, file=sys.stderr))
    producer.flush(0)          # debug only – remove once things work

def on_err(ws, err):           # same fix for on_err
    print("WS error:", err, file=sys.stderr)

# ⬇⬇  switched host: Binance.US is allowed from U.S. IPs
ws = websocket.WebSocketApp(
    "wss://stream.binance.us:9443/ws/btcusdt@trade",
    on_message=on_msg,
    on_error=on_err,
)

ws.run_forever(ping_interval=20, ping_timeout=10)