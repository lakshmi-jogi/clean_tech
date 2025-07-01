class SmartBin:
    def __init__(self, location, capacity_kg):
        self.location = location
        self.capacity = capacity_kg
        self.level = 0

    def add_waste(self, kg):
        if self.level + kg <= self.capacity:
            self.level += kg
            print(f"[{self.location}] Added {kg}kg waste. Current level: {self.level}/{self.capacity}kg")
        else:
            print(f"[{self.location}] Bin overflow! Cannot add {kg}kg.")

    def get_fill_percentage(self):
        return (self.level / self.capacity) * 100

    def is_full(self):
        return self.level >= self.capacity

    def empty_bin(self):
        print(f"[{self.location}] Bin emptied.")
        self.level = 0

def display_bin_status(bin_obj):
    print(f"\n Location: {bin_obj.location}")
    print(f" Fill Level: {bin_obj.level}/{bin_obj.capacity} kg ({bin_obj.get_fill_percentage():.1f}%)")
    print(" Status: " + ("Full" if bin_obj.is_full() else "Not Full"))
    print("-" * 30)

def run_simulation():
    bin1 = SmartBin("City Center", 10)
    bin2 = SmartBin("School Zone", 15)

    bin1.add_waste(3)
    bin1.add_waste(4)
    bin2.add_waste(5)
    bin2.add_waste(7)

    print("\n Smart Bin Monitoring Dashboard")
    display_bin_status(bin1)
    display_bin_status(bin2)

    for b in [bin1, bin2]:
        if b.is_full():
            b.empty_bin()

if __name__ == "__main__":
    run_simulation()
