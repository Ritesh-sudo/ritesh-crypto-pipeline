#!/usr/bin/env python3
"""
Consume messages from the raw_ticks topic and pretty-print them.
Run:  python consumer.py [--from-beginning]
"""
import argparse, json, time
from kafka import KafkaConsumer

parser = argparse.ArgumentParser()
parser.add_argument("--from-beginning", action="store_true",
                    help="start at earliest offset instead of latest")
args = parser.parse_args()

consumer = KafkaConsumer(
    "raw_ticks",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda b: json.loads(b.decode("utf-8")),
    auto_offset_reset="earliest" if args.from_beginning else "latest",
    enable_auto_commit=False,
)

for msg in consumer:
    tick = msg.value
    ts   = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tick["T"] / 1_000))
    print(f"[{ts}] {tick['symbol']} {tick['price']}")