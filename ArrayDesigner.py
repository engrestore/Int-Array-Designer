class ArrayDesigner:
    def __init__(self, initial_list):
        self.arr = initial_list;

    def add_int(self, value):
        self.arr.append(value);
        print(f"Added {value}. Current array: {self.arr}");

    def delete_max(self):
        if self.arr:
            max_val = max(self.arr);
            self.arr.remove(max_val);
            print(f"Deleted max ({max_val}). Current array: {self.arr}");
        else:
            print("Array is empty!");

    def delete_min(self):
        if self.arr:
            min_val = min(self.arr);
            self.arr.remove(min_val);
            print(f"Deleted min ({min_val}). Current array: {self.arr}");
        else:
            print("Array is empty!");

    def delete_number(self, value):
        if value in self.arr:
            self.arr.remove(value);
            print(f"Deleted {value}. Current array: {self.arr}");
        else:
            print(f"{value} not found in array!");

    def reorder_desc(self):
        self.arr.sort(reverse=True);
        print(f"Reordered descending: {self.arr}");

    def reorder_asc(self):
        self.arr.sort();
        print(f"Reordered ascending: {self.arr}");

    def check_array(self):
        print(f"Current array: {self.arr}");

def main():
    designer = ArrayDesigner([]);

    while True:
        print("\n--- Array Designer Menu ---");
        print("1. Add an integer");
        print("2. Delete maximum integer");
        print("3. Delete minimum integer");
        print("4. Delete a specific integer");
        print("5. Reorder ascending");
        print("6. Reorder descending");
        print("7. Check list")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ").strip();

        if choice == "1":
            try:
                val = int(input("Enter integer to add: "));
                designer.add_int(val);
            except ValueError:
                print("Invalid input. Please enter an integer.");
        elif choice == "2":
            designer.delete_max();
        elif choice == "3":
            designer.delete_min();
        elif choice == "4":
            try:
                val = int(input("Enter integer to delete: "));
                designer.delete_number(val);
            except ValueError:
                print("Invalid input. Please enter an integer.");
        elif choice == "5":
            designer.reorder_asc();
        elif choice == "6":
            designer.reorder_desc();
        elif choice == "7":
            designer.check_array();
        elif choice == "8":
            print("Exiting program.");
            break
        else:
            print("Invalid choice. Please select 1–8.");


if __name__ == "__main__":
    main();
