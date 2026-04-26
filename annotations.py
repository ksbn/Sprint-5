# Exercise: Add type annotations and fix all bugs mypy catches.
 
# Bugs found:
# 1. open_account("Tobi", 9.13)    — missing `balances` argument, amount is float not int
# 2. open_account("Olya", "£7.13") — missing `balances` argument, amount is str not int
# 3. format_pence_as_str()          — wrong name, should be format_pence_as_string()
 
def open_account(balances: dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount
 
def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total
 
def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"
 
balances: dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}
 
open_account(balances, "Tobi", 913)   # Fix 1: added balances, 9.13 → 913 pence
open_account(balances, "Olya", 713)   # Fix 2: added balances, "£7.13" → 713 pence
 
total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)  # Fix 3: corrected function name
 
print(f"The bank accounts total {total_string}")
 