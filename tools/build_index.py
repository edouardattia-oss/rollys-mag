#!/usr/bin/env python3
"""Valide les articles et régénère index.json (lu par rollyspub.com/mag/lib.php)."""
import json, re, sys, os, glob
from datetime import datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"billard", "flechettes", "guides"}
REQ = ["slug", "title", "description", "category", "date", "body", "sources"]
errors, items = [], []
for f in sorted(glob.glob(os.path.join(ROOT, "articles", "*.json"))):
    try:
        a = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        errors.append(f"{f}: JSON invalide ({e})"); continue
    name = os.path.basename(f)[:-5]
    for k in REQ:
        if not a.get(k) and k != "sources":
            errors.append(f"{name}: champ manquant {k}")
    if a.get("slug") != name: errors.append(f"{name}: slug différent du nom de fichier")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.get("slug", "")): errors.append(f"{name}: slug invalide")
    if a.get("category") not in CATS: errors.append(f"{name}: catégorie invalide")
    try: datetime.fromisoformat(a["date"]); datetime.fromisoformat(a.get("updated", a["date"]))
    except Exception: errors.append(f"{name}: date ISO invalide")
    if re.search(r"<script|<iframe|on\w+=", a.get("body", ""), re.I): errors.append(f"{name}: HTML interdit")
    if not (110 <= len(a.get("description", "")) <= 260): errors.append(f"{name}: description de {len(a.get('description',''))} caractères (110-260)")
    if a.get("type") == "news" and not a.get("sources"): errors.append(f"{name}: article d'actu sans sources")
    items.append({"slug": a.get("slug"), "updated": a.get("updated", a.get("date")), "date": a.get("date"), "category": a.get("category"), "title": a.get("title")})
try: json.load(open(os.path.join(ROOT, "agenda.json"), encoding="utf-8"))
except Exception as e: errors.append(f"agenda.json invalide ({e})")
if errors:
    print("ERREURS :\n- " + "\n- ".join(errors)); sys.exit(1)
old = {}
p = os.path.join(ROOT, "index.json")
if os.path.exists(p): old = json.load(open(p, encoding="utf-8"))
removed = sorted(set(old.get("removed", [])) | ({x["slug"] for x in old.get("articles", [])} - {x["slug"] for x in items}))
items.sort(key=lambda x: x["date"], reverse=True)
json.dump({"generated": datetime.now().isoformat(timespec="seconds"), "articles": items, "removed": removed}, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"OK : {len(items)} articles, index.json régénéré")
