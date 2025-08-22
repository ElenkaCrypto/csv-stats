import argparse, csv, statistics, sys
from typing import Iterable

def to_float(x:str):
    try:
        return float(x.replace(",", "."))  # простий кейс з комою
    except: 
        return None

def iter_vals(path:str, column:str|int, delimiter:str|None):
    with open(path, "r", encoding="utf-8", newline="") as f:
        if not delimiter:
            sample = f.read(2048)
            f.seek(0)
            try:
                delimiter = csv.Sniffer().sniff(sample).delimiter
            except: 
                delimiter = ","
        r = csv.reader(f, delimiter=delimiter)
        header = next(r, [])
        idx = int(column) if isinstance(column, int) or column.isdigit() else header.index(column)
        for row in r:
            if idx < len(row): 
                yield row[idx]

def main(argv=None):
    p = argparse.ArgumentParser(description="CSV column stats")
    p.add_argument("file")
    p.add_argument("column", help="name or index (0-based)")
    p.add_argument("-d", "--delimiter", help="custom delimiter, else auto")
    args = p.parse_args(argv)
    vals = [v for v in (to_float(x) for x in iter_vals(args.file, args.column, args.delimiter)) if v is not None]
    if not vals: sys.exit("no numeric data found")
    print(f"count: {len(vals)}")
    print(f"min: {min(vals)}")
    print(f"max: {max(vals)}")
    print(f"mean: {statistics.mean(vals)}")
    try: 
        print(f"median: {statistics.median(vals)}")
        print(f"stdev: {statistics.pstdev(vals)}")
    except statistics.StatisticsError:
        pass

if __name__ == "__main__":
    main()
