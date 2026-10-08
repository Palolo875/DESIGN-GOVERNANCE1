#!/usr/bin/env python3
"""Injecte les données extraites des sources dans le gabarit de la carte. Usage : construire_carte.py GABARIT DONNEES SORTIE"""
import json, sys
tpl, data, out = sys.argv[1:4]
d = json.dumps(json.load(open(data, encoding="utf-8")), ensure_ascii=False).replace("</", "<\\/")
open(out, "w", encoding="utf-8").write(open(tpl, encoding="utf-8").read().replace("__DATA__", d))
