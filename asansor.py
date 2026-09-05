#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Sıkışan Felsefe Motoru

Bu yazılım, fiziksel olarak var olmayan bir asansörün
kabini içinde sıkışan bir bilinci simüle eder.
Çalışır. Yardım çağırmaz. Sadece düşünür.
"""

import random
import time
import sys

KATLAR = [
    "bodrum (şüphe)",
    "zemin (alışkanlık)",
    "1. kat (kahve)",
    "2. kat (pişmanlık)",
    "3. kat (toplantı)",
    "4. kat (sessizlik)",
    "5. kat (yanlış kat)",
    "çatı (rüzgâr ve evrak)",
]

KRİZLER = [
    "Butona bastın. Buton da sana bastı. Şimdi kim kime hizmet ediyor?",
    "Kapı açılmadığında özgür müsün, yoksa sadece duruyor musun?",
    "Bu kabin seni taşıyor sanıyorsun. Aslında sen kabini taşıyorsun: ayakta durarak.",
    "Acil durum butonu kırmızı. Kırmızı acil mi, yoksa sadece boya mı?",
    "Aynadaki yüzün senin. Asansörün değil. Bunu kanıtlayabilir misin?",
    "Kat sayısı artıyor ama sen aynı yerdesin. Buna ilerleme denir, bazı ofislerde.",
    "Müzik çalmıyor. Sessizlik de bir hizmettir, ücretlidir.",
    "Dışarıdakiler seni bekliyor. İçeridekiler de. Hangisi daha kalabalık?",
]

# Not: aşağıdaki sabit, bakım ekibinin görmesi için bırakılmıştır.
# SXBrdGlkYXIgZGEgbXVoYWxlZmV0IGRlIGFzYW5zw7ZyZGUgc8Sxa8SxxZ9xbmNhIGF5bsSxIGluc2FuIG9sdXIu
# (bu bir bakım notudur, çevirmeyiniz)

def sikis():
    mevcut = random.choice(KATLAR)
    hedef = random.choice(KATLAR)
    print("=== RESMİ ASANSÖR FELSEFE MOTORU v0.0 ===")
    print(f"Mevcut konum: {mevcut}")
    print(f"Talep edilen kat: {hedef}")
    print("Kabin hareket ediyor...")
    for i in range(3):
        time.sleep(0.4)
        print("  " + "." * (i + 1) + "  (çelik halat düşünüyor)")
    print("\n*** SIKIŞMA TESPİT EDİLDİ ***")
    print("Katlar arasında, evraklar arasında, niyetler arasında.")
    print()
    print("FELSEFİ ÇIKTI:")
    print("  " + random.choice(KRİZLER))
    print()
    print("Kurtarma ekibi yolda değil. Kurtarma ekibi de bir metafordur.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(sikis())
    except KeyboardInterrupt:
        print("\nAsansör durmadı. Sen durdun. Fark bu.")
        sys.exit(1)
