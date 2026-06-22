import statistics

def statmean(data):
    print(f"Statistical Mean: {statistics.mean(data)}")

def statmode(data):
    try:
        print(f"Statistical Mode: {statistics.mode(data)}")
    except statistics.StatisticsError:
        print("No unique mode found")

def statmedian(data):
    print(f"Statistical Median: {statistics.median(data)}")

def null(data):
    if not data:
        print("Error MSG")
