#!/usr/bin/env python3
import subprocess

def main():
    try:
        print("Top 5 CPU Processes:\n")
        lines = subprocess.check_output("ps -Ao pid,%cpu,comm | sort -rn -k2 | head -n 6", shell=True).decode().strip().split("\n")[1:]
        for i in range(len(lines)):
            line = lines[i]
            try:
                _, cpu, comm = line.split(None, 2)
                name = comm.split("/")[-1]
                print(f"{name} - {cpu}%")
            except ValueError:
                continue
    except Exception:
        print("Failed to fetch top CPU processes.")

if __name__ == "__main__":
    main()
